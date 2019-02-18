import boto3

if __name__ == "__main__":

   
    collectionId='photos'
    faces=[]
    faces.append("373ce3fd-c2e0-410d-ba78-9023e2216f76")

    client=boto3.client('rekognition',region_name='us-east-1')

    response=client.delete_faces(CollectionId=collectionId,
                               FaceIds=faces)
    
    print(str(len(response['DeletedFaces'])) + ' faces deleted:')                           
    for faceId in response['DeletedFaces']:
         print (faceId)