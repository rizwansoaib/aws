import boto3
s3 = boto3.resource('s3')
data = open('gullu1.jpg', 'rb')
s3.Bucket('s3name').put_object(Key='s3name.jpg', Body=data)