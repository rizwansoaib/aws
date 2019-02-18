import boto3
client = boto3.client('rekognition',region_name='us-east-1') 
a=['badal','ghulaam','rizwan','diwakar','sailesh']
absent,present=[],[] 
for x in a:
	
	with open('photo.jpg', 'rb') as target_image:
	  target_bytes = target_image.read()
	response = client.compare_faces(
	               SourceImage={
			"S3Object": {
				"Bucket": "rizwans3",
				"Name": x+".jpg",
			}
		},
	               TargetImage={ 'Bytes': target_bytes },)   
	if len(response['FaceMatches'])>0:per=response['FaceMatches'][0]['Similarity']
	else:per=80   
	if(int(per)>85):
		print("Attendence has been granted to "+x)
		present.append(x)
	else:
		print("Attendence has not granted to "+x)
		absent.append(x)

print("present student list: ")
for x in present:
	print(x,end=" ")

print("\nabsent student list: ")
for x in absent:
	print(x,end=" ")
	
