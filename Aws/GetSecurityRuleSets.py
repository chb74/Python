# -- By liverpools@gmail.com -- # 
# -- On Feb 26, 2018 -- # 

import boto3 
from Libs import GetClient

VpcId = 'vpc-xxxxx'
SecurityGroup = 'Prd-Web-SG'

def GetRuleSets(**Params):
    client = GetClient("ec2")
    response = None
    try:

        response = client.describe_security_groups(
            Filters = [
                {
                    'Name': 'group-name',
                    'Values': [
                        Params['GroupName'],
                    ],
                }
            ],
        )
    except Exception as e:
        print(e)
    return response['SecurityGroups']
    
if __name__ == "__main__":

    Params = {}
    Rules = [] 
    Params.update({'Name': 'vpc-id'})
    Params.update({'Values': VpcId  })
    Params.update({'GroupName': SecurityGroup})

    count = 1
    response = GetRuleSets(**Params)
    for i in response:
        for j in i['IpPermissions']:
            print(j)
            for k in j['IpRanges']:
                if k['CidrIp']:
                    Rules.append([j['IpProtocol'], j['FromPort'], j['ToPort'], k['CidrIp'], k['Description']])
                    print(count ,"=>", j['IpProtocol'], j['FromPort'], j['ToPort'], k['CidrIp'], k['Description'])
                else:
                    for l in j['UserIdGroupPairs']:
                        Rules.append([j['IpProtocol'], j['FromPort'], j['ToPort'], k['CidrIp'], k['Description']])
                        print(count ,"=>", j['IpProtocol'], j['FromPort'], j['ToPort'], k['CidrIp'], k['Description'])

