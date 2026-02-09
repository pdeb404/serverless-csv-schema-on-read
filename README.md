# Automating Schema-on-Read Data Ingestion in Serverless Systems for Ad-Hoc SQL Analytics

## Overview
This project implements a serverless, event-driven data ingestion and analytics pipeline for CSV files using AWS cloud services. 
The system automatically processes uploaded CSV files, performs data cleaning and transformation, generates data quality metrics, 
and enables ad-hoc SQL analytics without using servers or traditional databases.

## Problem Statement
Organizations frequently receive structured data in CSV format. Manually processing and validating these files is error-prone 
and does not scale. Traditional database-centric approaches introduce infrastructure overhead and cost for small to medium workloads.
This project addresses the problem by designing a cost-aware, serverless architecture that automates CSV ingestion and supports 
schema-on-read analytics.

## Key Features
- Automated CSV ingestion triggered by file uploads
- Serverless data cleaning and transformation
- Schema-on-read analytics using SQL
- Integrated data quality auditing (valid and invalid records)
- Fully event-driven and AWS Free Tier–friendly

## Architecture Overview
The pipeline follows an event-driven serverless architecture:
1. CSV files are uploaded to Amazon S3
2. S3 events trigger an AWS Lambda function
3. Lambda processes data and generates audit metrics
4. AWS Glue catalogs schema metadata
5. Amazon Athena enables SQL-based analytics directly on S3 data

## Technologies Used
- Amazon S3
- AWS Lambda
- AWS Glue Data Catalog
- Amazon Athena
- AWS IAM
- Amazon CloudWatch

## Repository Structure
This repository contains:
- Lambda source code
- Architecture diagrams
- Sample input and output data
- SQL queries for analytics
- Step-by-step deployment and demo documentation

## Deployment
The system is deployed using AWS serverless services via the AWS Management Console. 
Detailed setup instructions are provided in the documentation folder.

## Notes
This repository documents the implementation and design of the system. 
Execution requires an AWS account to provision the required serverless resources.
