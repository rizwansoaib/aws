
import boto3

if __name__ == "__main__":
    
    maxResults=2
    collectionId='collection-name'
	
    client=boto3.client('rekognition',region_name='us-east-1')

 
    print('Creating collection:' + collectionId)
    response=client.create_collection(CollectionId=collectionId)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
