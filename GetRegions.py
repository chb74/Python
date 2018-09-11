# -- By liverpools@gmail.com -- # 
# -- On Mar 09, 2018 -- # 

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_regions()

for regions in response['Regions']:
    print(regions)
