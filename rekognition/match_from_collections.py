import boto3

if __name__ == "__main__":

    bucket='rizwans3'
    collectionId='photos'
    fileName='rizwan.jpg'
    threshold = 70
    maxFaces=2

    client=boto3.client('rekognition',region_name='us-east-1')

  
    response=client.search_faces_by_image(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            