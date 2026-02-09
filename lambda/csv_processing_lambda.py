import csv
import boto3
import io
from datetime import datetime

s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    response = s3.get_object(Bucket=bucket, Key=key)
    data = response["Body"].read().decode("utf-8")

    reader = csv.DictReader(io.StringIO(data))
    output = io.StringIO()

    fieldnames = reader.fieldnames + ["grade"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    total_rows = 0
    valid_rows = 0

    for row in reader:
        total_rows += 1
        if row["marks"]:
            marks = int(row["marks"])
            row["grade"] = "A" if marks >= 80 else "B"
            writer.writerow(row)
            valid_rows += 1

    # write processed CSV
    s3.put_object(
        Bucket="csv-processed-progyan",
        Key="cleaned/student_data_processed.csv",
        Body=output.getvalue()
    )

    # write audit CSV
    audit_output = io.StringIO()
    audit_writer = csv.writer(audit_output)
    audit_writer.writerow([
        "source_file",
        "total_rows",
        "valid_rows",
        "invalid_rows",
        "processed_at"
    ])
    audit_writer.writerow([
        key,
        total_rows,
        valid_rows,
        total_rows - valid_rows,
        datetime.utcnow().isoformat()
    ])

    s3.put_object(
        Bucket="csv-processed-progyan",
        Key="audit/pipeline_audit.csv",
        Body=audit_output.getvalue()
    )

    return {"status": "success"}
