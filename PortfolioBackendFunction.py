import boto3
import json
from decimal import Decimal
#import os

## Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj) 


#DEFAULT_REGION = "eu-west-2"
#region_name = os.environ.get("AWS_REGION", DEFAULT_REGION)

def lambda_handler(event, context):  

    dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
   
    table = dynamodb.Table('VisitorCounter')

    response = table.get_item(
        Key={
            'website': 'joshmearsportfolio'
        }
    )
    count = response['Item']

    count['visitors'] += 1
        
    table.put_item(Item=count)

    response = table.get_item(
        Key={
            'website': 'joshmearsportfolio'
        }
    )
    
    count = response['Item']

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET",
            "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps(count, cls=DecimalEncoder)
    }

