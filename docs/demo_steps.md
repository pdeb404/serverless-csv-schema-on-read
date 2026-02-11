# Live Demo Walkthrough

This guide explains how to demonstrate the system end-to-end.

## Step 1: Show Raw Data Bucket

- Open Amazon S3
- Navigate to the raw data bucket
- Open the uploads/ folder

## Step 2: Upload Sample CSV

Upload:
data/input/student_data_raw.csv

Explain:
Uploading the file triggers automatic processing.

## Step 3: Show Lambda Execution

- Open AWS Lambda
- Go to Monitor → CloudWatch Logs
- Show latest execution log

Explain:
The Lambda function executed automatically via S3 event notification.

## Step 4: Show Processed Output

- Open processed bucket
- Navigate to cleaned/
- Open student_data_processed.csv

Explain:
Data cleaning and transformation completed successfully.

## Step 5: Show Audit Metrics

- Open audit/
- Open pipeline_audit.csv

Explain:
Data quality metrics were generated during processing.

## Step 6: Run Athena Query

Run:
SELECT department, AVG(marks)
FROM cleaned
GROUP BY department;

Explain:
Athena performs SQL queries directly on S3 using schema-on-read.

## Step 7: Show Audit Query

Run:
SELECT source_file, invalid_rows
FROM audit;

Explain:
Audit metrics can also be analyzed using SQL.
