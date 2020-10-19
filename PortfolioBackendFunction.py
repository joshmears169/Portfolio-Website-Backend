import boto3
import json
   
def lambda_handler(event, context):  

    dynamodb = boto3.resource('dynamodb')
   
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
            "Access-Control-Allow-Origin": "*"
        },
        "body": count
    }

