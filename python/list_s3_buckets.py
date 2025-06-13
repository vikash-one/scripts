import boto3

s3 = boto3.client('s3')
for b in s3.list_buckets()["Buckets"]:
    print(f"{b['Name']} - Created on {b['CreationDate']}")
