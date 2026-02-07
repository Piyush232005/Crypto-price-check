🚀 COMPLETE PROJECT PACKAGE — Crypto Price Monitoring System

1. GitHub Repository Structure

Create repo like this

crypto-price-monitoring-aws/
│
├── lambda-fetch-price/
│   └── lambda_store_price.py
│
├── lambda-api-fetch/
│   └── lambda_fetch_api.py
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│
├── screenshots/
│   ├── dynamodb-table.png
│   ├── sns-alert.png
│   ├── api-output.png
│
├── README.md
├── DEPLOYMENT.md
├── LICENSE

🚀 AWS Serverless Crypto Price Monitoring System
📌 Overview

This project is a Serverless Cryptocurrency Monitoring System built using AWS cloud services. It automatically tracks Ethereum price in real time, stores historical data, sends alerts, and provides public API access

🧱 Tech Stack

AWS Lambda

Amazon DynamoDB

Amazon SNS

Amazon EventBridge

Amazon API Gateway

Python

CoinGecko API


⚙️ System Workflow

EventBridge Scheduler
        ↓
Lambda Fetch Price
        ↓
SNS Email Alerts
        ↓
DynamoDB Storage
        ↓
API Gateway
        ↓
Lambda Fetch API
        ↓
Frontend / Users

🛠️ Implementation Steps

🔹 Step 1 — Created Lambda Function

Built Python Lambda function to fetch Ethereum price from CoinGecko And a alert function which give notification of crypto via SNS AWS service.

🔹 Step 2 — Connected CoinGecko API

Used public crypto API for real-time price data.

🔹 Step 3 — Integrated Amazon SNS

Created SNS topic to send email alerts for price updates.

🔹 Step 4 — Setup EventBridge Scheduler

Configured automatic execution every few minutes.


🔹 Step 5 — Configured IAM Roles

Added secure permissions:

SNS Publish

DynamoDB Access

CloudWatch Logs


🔹 Step 6 — Created DynamoDB Table

Table Name: crypto_price_history
Partition Key: coin_id
Sort Key: timestamp


🔹 Step 7 — Stored Price Data

Lambda stores:

ETH USD price

ETH INR price

Timestamp

🔹 Step 8 — Created API Lambda

Fetches latest ETH price data from DynamoDB.

🔹 Step 9 — Setup API Gateway

Created public REST endpoint 

GET /eth-data

🔹 Step 10 — Enabled CORS

Allowed external applications to fetch API data.


🔹 Step 11 — Tested Complete System

System now supports:

✔ Automatic price monitoring
✔ Historical data storage
✔ Email alerts
✔ Public API

📊 Sample API Response

{
  "data": {
    "eth_usd": 2432.19,
    "eth_inr": 201871.77,
    "timestamp": "2026-02-01T06:32:30"
  }
}


🔐 Security

IAM Role Based Access

Serverless Security Model

No Hardcoded Credentials

📈 Scalability Benefits

Auto Scaling Lambda

Managed NoSQL Storage

Event Driven Architecture

📈 Scalability Benefits

Auto Scaling Lambda

Managed NoSQL Storage

Event Driven Architecture


👨‍💻 Author

Piyush 

Description

Developed a scalable serverless cryptocurrency monitoring system using AWS Lambda, DynamoDB, SNS, API Gateway, and EventBridge to track real-time Ethereum price and expose API endpoints for external consumption.