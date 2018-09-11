# -- By liverpools@gmail.com -- # 
# -- On Jan 18, 2018 -- # 

import boto3, time, json
from pprint import pprint


# -- You must be define about VPC -- # 
VpcName = 'Prd-Mz-VPC'
TmpFileName = './Datas/' + VpcName + '.json'
Service = 'ec2'
Region  = 'ap-northeast-2'
Profile = 'default'

# -- This is a Session for AWS Connection -- # 
def GetClient(Service = Service, Region = Region, Profile = Profile):
    session = boto3.Session(profile_name = Profile)
    client = session.client(Service, Region)
    
    return client

# -- Getting about VPC information -- # 
def GetVpcs(VpcName):
    client = GetClient()
    response = None

    try:
        response = client.describe_vpcs(Filters=[{'Name':'tag-value','Values': [ VpcName,]}])
    except Exception as e:
        print(e)
    return response

# -- Getting about Internet Gateway information -- # 
def GetInternetGateway(VpcId):
    client = GetClient() 
    response = ''
    try:
        response = client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [VpcId,]}])
    except Exception as e:
        print(e)
    for igw in response['InternetGateways']:
        return igw['InternetGatewayId']

# -- Getting about Subnet information -- # 
def GetSubnets(VpcId):
    response = None 
    client = GetClient()

    try:
        response = client.describe_subnets(Filters=[{'Name':'vpc-id','Values':[VpcId,]}])
    except Exception as e:
        print(e)
    return response

# -- Getting about SecurityGroup information -- # 
def GetSecurityGroups(VpcId):
    response = None 
    client = GetClient()
    try:
        response = client.describe_security_groups(Filters=[{'Name':'vpc-id', 'Values': [VpcId,]}])
    except Exception as e:
        print(e)

    return response

# -- Getting about Route Tables information -- #
def GetRouteTables(VpcId):
    response = None 
    client = GetClient()

    try:
        response = client.describe_route_tables(Filters=[{'Name':'vpc-id', 'Values': [VpcId, ] } ])
    except Exception as e:
        print(e)
    
    return response

# -- Getting about Network Acls information -- # 
def GetNetworkAcls(VpcId):
    response = None 
    client = GetClient()

    try:
        response = client.describe_network_acls(Filters=[ { 'Name': 'vpc-id', 'Values': [VpcId,] } ])
    except Exception as e:
        print(e)

    return response 

if __name__ == "__main__":
    BeginTime = time.time() 
    response = GetVpcs(VpcName)
    Vpc = {}
    Subnets = []
    SecurityGroups = [] 
    RouteTables = [] 
    NetworkAcls = [] 

    # -- Collect information of VPC -- # 
    for vpc in response['Vpcs']:
        for v in vpc['Tags']:
            Vpc.update({'VpcName': VpcName, 'VpcId': vpc['VpcId'], 'CidrBlock': vpc['CidrBlock']})
#    response = GetSubnets()
    Igw = GetInternetGateway(Vpc['VpcId'])
    Vpc.update({'InternetGatewayId': Igw})
# --   print(Vpc)
    res = GetSubnets(Vpc['VpcId'])

    for s in res['Subnets']:
        for subnet in s['Tags']:
            Subnets.append({'SubnetName': subnet['Value'], 'SubnetId': s['SubnetId'], 'SubnetCidrBlock': s['CidrBlock']})
# --   pprint(Subnets)
    res = GetSecurityGroups(Vpc['VpcId'])

    for s in res['SecurityGroups']:
        SecurityGroups.append({'SecurityGroupName': s['GroupName'], 'SecurityGroupId': s['GroupId']})


    res = GetRouteTables(Vpc['VpcId'])
    for r in res['RouteTables']:
        for t in r['Tags']:
            RouteTables.append( { 'RouteTableId': r['RouteTableId'], 'RouteTableName': t['Value'] } )
           
    res = GetNetworkAcls(Vpc['VpcId'])
    for r in res['NetworkAcls']:
        for t in r['Tags']:
            NetworkAcls.append({'NetworkAclName': t['Value'], 'NetworkAclId': r['NetworkAclId']})
    Vpcs = {
        "Vpc": Vpc,
        "Subnets" : Subnets,
        "RouteTables": RouteTables,
        "SecurityGroups":SecurityGroups,
        "NetworkAcls": NetworkAcls 
    }
    
    # -- Write a information of vpc -- # 
    with open(TmpFileName, "w", encoding='utf8') as f:
        data = json.dumps(Vpcs, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
        f.write(data)

    print(" * It tooks %s seconds " % (time.time() - BeginTime))
