import json
import urllib.request
import boto3
from datetime import datetime
from decimal import Decimal

# ---- CONFIG ----
TABLE_NAME = "crypto_price_history"
SNS_TOPIC_ARN = "Paste your sns arn here"
USD_TO_INR = Decimal("83")

# ---- AWS Clients ----
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

sns = boto3.client("sns")

# ---- Helper ----
def to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

# ---- Lambda Handler ----
def lambda_handler(event, context):

    # Fetch ETH price from CoinGecko
    url = "pasre ypur api url here"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    eth_usd = Decimal(str(data["ethereum"]["usd"]))
    eth_inr = eth_usd * USD_TO_INR
    timestamp = datetime.utcnow().isoformat()

    # ---- Store in DynamoDB ----
    table.put_item(
        Item={
            "coin_id": "ETH",
            "timestamp": timestamp,
            "price_usd": eth_usd,
            "price_inr": eth_inr
        }
    )

    # ---- Send SNS Notification ----
    message = f"""
🚨 Ethereum Price Alert

USD Price: ${eth_usd}
INR Price: ₹{eth_inr}
Time: {timestamp}
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Ethereum Price Update",
        Message=message
    )

    # ---- API Response ----
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "data": {
                "eth_usd": to_float(eth_usd),
                "eth_inr": to_float(eth_inr),
                "timestamp": timestamp
            }
        })
    }
