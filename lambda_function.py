import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # Copied from https://repost.aws/questions/QUDQfUTdRpT9-i09eULZIqDQ/listing-the-objects-in-a-s3-bucket-in-a-lambda-python-function
    bucket = s3.Bucket('my-test-bucket-mykhailo')
    for obj in bucket.objects.all():
        print(obj.key)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
