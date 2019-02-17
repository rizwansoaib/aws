import boto3
import botocore

BUCKET_NAME = 's3name' 
KEY = 'object-name-s3.jpg' 
s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'download-name.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
 