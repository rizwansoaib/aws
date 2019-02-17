import boto3
s3 = boto3.resource('s3')
s3.Object('s3bucketname','s3name.jpg').upload_file(Filename='input.jpg')