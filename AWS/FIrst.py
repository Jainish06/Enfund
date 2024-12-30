#Write an AWS Lambda function that adds two numbers and returns the result.

import json

def lambda_handler(event, context):
    a = float(event.get('a', 0))
    b = float(event.get('b', 0))
    sum = a + b
    return {
        'statusCode': 200,
        'body': json.dumps({
            'a': a,
            'b': b,
            'sum': sum
        })
    }