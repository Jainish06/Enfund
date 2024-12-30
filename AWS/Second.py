#Code an AWS Lambda function to store a document or PDF file in an S3 bucket.


⁠import boto3
import base64

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket = event['bucket_name']
    filename = event['file_name']
    content = base64.b64decode(event['file_content'])
    s3_client.put_object(Bucket=bucket, Key=filename, Body=content)
    return {
        'statusCode': 200,
        'body': f"File {filename} uploaded successfully to bucket {bucket}."
    }