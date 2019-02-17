
import logging
import boto3
from botocore.exceptions import ClientError


def list_bucket_objects(bucket_name):
    

    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
       
        logging.error(e)
        return None
    return response['Contents']


def main():

    test_bucket_name = 's3-name'

 
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')


    objects = list_bucket_objects(test_bucket_name)
    if objects is not None:
      
        logging.info(f'Objects in {test_bucket_name}')
        for obj in objects:
            logging.info(f'  {obj["Key"]}')


if __name__ == '__main__':
    main()