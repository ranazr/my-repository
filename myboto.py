import boto3

#sts example
sts = boto3.client('sts')

response = sts.get_caller_identity()

print(response)


#s3 example
# s3 =boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)


# #ec2 example
# ec2 =boto3.resource('ec2')

# for instance in ec2.instances.all():
#     print(instance.id, instance.state)


#another ec2 example
#ec2 = boto3.resource('ec2')

# ec2.create_instances(
#     ImageId='ami-09d95fab7fff3776c',
#     MinCount=1,
#     MaxCount=2,
#     InstanceType='t2.micro'


