import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

TABLE_NAME = "crypto_price_history"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def lambda_handler(event, context):

    response = table.query(
        KeyConditionExpression=Key("coin_id").eq("ETH"),
        ScanIndexForward=False,
        Limit=1
    )

    items = response.get("Items", [])

    if not items:
        return {
            "statusCode": 404,
            "body": json.dumps({"data": None})
        }

    item = items[0]

    eth_usd = to_float(item["price_usd"])
    eth_inr = to_float(item["price_inr"])
    timestamp = item["timestamp"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "data": {
                "eth_usd": eth_usd,
                "eth_inr": eth_inr,
                "timestamp": timestamp
            }
        })
    }
