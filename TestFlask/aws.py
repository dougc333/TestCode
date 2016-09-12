import boto3


client=boto3.client('ec2')
print client
response = client.describe_image_attribute(DryRun=False, ImageId='ami-7b386c11', Attribute='description')
print response


#ec2 = boto3.resource('ec2')
#ec2.create_instances(ImageId='ami-7b386c11', MinCount=1, MaxCount=1)
#how to start




while(True):
	instances = ec2.instances.filter(
    	Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
	for instance in instances:
    		print(instance.id, instance.instance_type)


