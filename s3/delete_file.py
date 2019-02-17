import logging
import boto3
from botocore.exceptions import ClientError


def delete_object(bucket_name, object_name):
    
    s3 = boto3.client('s3')
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():

    test_bucket_name = 's3-name'
    test_object_name = 'file-name'


    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')


    if delete_object(test_bucket_name, test_object_name):
        logging.info(f'{test_object_name} was deleted from {test_bucket_name}')


if __name__ == '__main__':
    main()