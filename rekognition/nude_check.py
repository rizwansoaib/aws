import boto3

if __name__ == "__main__":

   
    photo='nude.jpg'
    bucket='rizwans3'
    
    client=boto3.client('rekognition',region_name='us-east-1')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
 