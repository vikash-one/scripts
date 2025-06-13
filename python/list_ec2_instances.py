import boto3

ec2 = boto3.client('ec2')
resp = ec2.describe_instances()

for res in resp['Reservations']:
    for inst in res['Instances']:
        print(f"{inst['InstanceId']} - {inst['State']['Name']} - {inst.get('InstanceType')}")
