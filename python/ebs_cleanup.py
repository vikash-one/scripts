import boto3

ec2 = boto3.client('ec2')
vols = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
for v in vols['Volumes']:
    print(f"Deleting volume {v['VolumeId']}")
    ec2.delete_volume(VolumeId=v['VolumeId'])
