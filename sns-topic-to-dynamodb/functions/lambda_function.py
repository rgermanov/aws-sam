import os
import json
import boto3

TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    # Get the SNS message from the event
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # Put the message into the DynamoDB table
    dynamodb.put_item(
        TableName=TABLE_NAME,
        Item={
            'MessageId': {'S': message['MessageId']},
            'MessageBody': {'S': message['MessageBody']}
        }
    )
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps('Message saved to DynamoDB')
    }
