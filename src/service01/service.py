import json
from tools import my_side_tool

print("Loading function")

def handler(event, context):

    # Call the function from the side_tools package
    my_side_tool()

    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda Service 01!')
        }

