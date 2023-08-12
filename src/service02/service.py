import json

import os
 
print("Loading function")

def handler(event, context):
    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda Service 02!')
        }

