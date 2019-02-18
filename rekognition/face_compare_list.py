import boto3
client = boto3.client('rekognition',region_name='us-east-1') 
a=['badal','ghulaam','rizwan','diwakar','sailesh']
absent,present=[],[] 
for x in a:
	with open(x+".jpg", 'rb') as source_image:
	  source_bytes = source_image.read()
	with open('photo.jpg', 'rb') as target_image:
	  target_bytes = target_image.read()
	response = client.compare_faces(
	               SourceImage={ 'Bytes': source_bytes },
	               TargetImage={ 'Bytes': target_bytes },)   
	if len(response['FaceMatches'])>0:per=response['FaceMatches'][0]['Similarity']
	else:per=80   
	if(int(per)>85):
		print("Attendence has been granted to "+x)
		present.append(x)
	else:
		print("Attendence not granted to "+x)
		absent.append(x)

print("present student list:\n")
for x in present:
	print(x+"\t")

print("absent student list:\n")
for x in absent:
	print(x+"\t")
	
