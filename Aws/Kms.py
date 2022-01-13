
import boto3 

client = boto3.client("kms")
#response = client.describe_key()
response = client.list_keys()

for i in response['Keys']:
    print(i)