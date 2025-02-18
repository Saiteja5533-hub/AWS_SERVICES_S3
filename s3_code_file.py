import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")




import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.client('s3', region_name=region)

bucket_name = 'saitejabucket55338896'

try:
    # Create the S3 bucket
    response = s3_client.list_buckets()
    for bucket in response["Buckets"]:
     print(bucket["Name"])

except ClientError as e:
    print(f'Error creating bucket: {e}')



    import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.resource('s3', region_name=region)

bucket_name = 'saitejabucket55338896'

try:
    # Read the S3 bucket

# Retrieve the list of existing buckets
    for bucket in s3_client.buckets.all():
      print(bucket.name)

except ClientError as e:
    print(f'Error creating bucket: {e}')