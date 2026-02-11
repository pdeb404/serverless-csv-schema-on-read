# Setup Guide: S3 and IAM Configuration

## Step 1: Create S3 Buckets

Create two Amazon S3 buckets:

1. Raw Data Bucket
   - Name: csv-raw-<your-name>
   - Public Access: Block all public access
   - Folder: uploads/

2. Processed Data Bucket
   - Name: csv-processed-<your-name>
   - Public Access: Block all public access
   - Folders:
     - cleaned/
     - audit/

## Step 2: Create IAM Role for Lambda

1. Go to AWS IAM → Roles → Create Role
2. Select trusted entity: AWS Service → Lambda
3. Attach policies:
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
4. Role Name:
   lambda-csv-processing-role

## Step 3: Create IAM Role for Glue Crawler

1. Create a new role
2. Trusted entity: AWS Service → Glue
3. Attach policies:
   - AmazonS3ReadOnlyAccess
   - AWSGlueServiceRole
4. Role Name:
   AWSGlueServiceRole-csv-crawler
