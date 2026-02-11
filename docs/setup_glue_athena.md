# Setup Guide: Glue Crawler and Athena Configuration

## Step 1: Create Glue Crawler

1. Go to AWS Glue → Crawlers → Create Crawler
2. Crawler name:
   csv-processed-crawler

## Step 2: Add Data Sources

Add two S3 data sources:

1. Processed data:
   s3://csv-processed-<your-name>/cleaned/

2. Audit metrics:
   s3://csv-processed-<your-name>/audit/

## Step 3: Assign IAM Role

Use:
AWSGlueServiceRole-csv-crawler

## Step 4: Create Database

Database name:
csv_pipeline_db

Run the crawler.

After completion, two tables should appear:
- cleaned
- audit

## Step 5: Configure Athena

1. Open Amazon Athena
2. Set query result location to:
   s3://csv-processed-<your-name>/athena-results/

3. Select database:
   csv_pipeline_db

## Step 6: Run Sample Queries

Example queries are provided in:
athena/sample_queries.sql
