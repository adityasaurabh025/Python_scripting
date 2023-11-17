import logging
import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        # Initialize the S3 client
        s3 = boto3.client('s3', region_name=region)

        # Create S3 bucket
        s3.create_bucket(Bucket=bucket_name)

        print(f"S3 bucket '{bucket_name}' created successfully!")

    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Bucket '{bucket_name}' already exists and is owned by you.")
        elif e.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f"Bucket '{bucket_name}' already exists. Choose a different name.")
        else:
            print(f"An error occurred: {e}")

# Replace 'your-unique-bucket-name' with your desired bucket name
bucket_name = 'demobucket740'

# Call the function to create the bucket
create_s3_bucket(bucket_name)