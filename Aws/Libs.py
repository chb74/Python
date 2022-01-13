# -- chb@mz.co.kr -- # 
# -- Dec 8, 2017 -- # 
# -- FileName : Libs.py -- # 
# -- Comments : 
# --    Begin VPC Information 
# --        Latest Modify : Jan 10, 2022 

TimeDelay = 0.4

# -- This is a Session for AWS Connection -- # 
def GetClient(Service = "ec2", Region = "ap-northeast-2", Profile = "default"): 
    session = boto3.Session(profile_name = Profile)
    client = session.client(Service, Region)
    return client

# -- This Function creates Tags about Resource -- #
def CreateTags(Resource, Key = "Name", Value, **Params):

    time.sleep(TimeDelay)
    client = GetClient(Service = "ec2", Region = "ap-northeast-2", Profile = "default")
    Tags = {}
    try:
        Tags = client.create_tags(
            Resources = [ Resource ],
            Tags=[{'Key':Key, 'Value': Value}]
        )
    except Exception as e:
        print(e)
    return Tags

def CreateDefaultRole():
    DefaultRole = ['Ec2Role', 'S3Role', 'LambdaRole']

    client = GetClient(Service = 'iam') 
    response = client.create_role(RoleName)

    return response 


# -- Get Id from Tag -- # 
def GetIdFromTag(Object, Tag, **Params):
    client = GetClient("ec2", Params['Region'], Params['Profile'])
    if 'sg' == Object:
        id = client.describe_security_groups( 
            Filters=[ 
                { 
                    'Name':'group-name', 
                    'Values': [Tag]
                },
                {
                    'Name':'vpc-id',
                    'Values': [ Params['VpcId']]
                }
            ],
        )
        for i in id['SecurityGroups']:
            return i['GroupId']

    elif 'sn' == Object:
#        client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
        id = client.describe_subnets( 
            Filters=[ 
                { 
                    'Name':'tag:Name', 
                    'Values': [Tag] 
                },
                {
                    'Name':'vpc-id',
                    'Values': [ Params['VpcId'] ]
                }
            ],
        )
        for s in id['Subnets']:
            return s['SubnetId']

    elif 'vpc' == Object: 
#        client = GetClient(Service, Region, Profile)
        id = client.describe_vpcs( Filters=[ { 'Name':'tag:Name', 'Values': [Tag], }, ],)
        for v in id['Vpcs']:
            return v['VpcId']
    elif 'rt' == Object:
        id = client.describe_route_tables(
            Filters = [ 
                {
                    'Name': 'tag:Name',
                    'Values': [ Tag ]
                },
                {
                    'Name': 'vpc-id',
                    'Values': [ Params['VpcId'] ]

                }
            ]
        )
        for v in id['RouteTables']:
            return v['RouteTableId']
    elif "igw" == Object:
        id = client.describe_internet_gateways(
            Filters = [
                {
                    'Name': 'tag:Name',
                    'Values': [ Tag ]
                },
            ]
        )
        for v in id['InternetGateways']:
            return v['InternetGatewayId']
    else:
        pass

    return None

# -- Change the name to ID -- # 
def ChangeId(Type, Value, data, Elb):
    # -- -- # 
    if Type == "sg":
        for i in data:
            if Elb == False:
                if Value == i['SecurityGroupName'] and 'Alb' not in i['SecurityGroupName'] and 'Elb' not in i['SecurityGroupName']:
                    return i['SecurityGroupId']
            else:
                if Value == i['SecurityGroupName'] and 'Elb' in i['SecurityGroupName']:
                    return i['SecurityGroupId']
    else:
        for i in data:
            if Value in i['SubnetName']:
                return i['SubnetId']

# -- Get information of Vpc -- # 
def GetVpcId(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
    response = None 
    Vpcs = []

    try:
        response = client.describe_vpcs()
    except Exception as e:
        print(e)

    for i in response['Vpcs']:
        for j in i['Tags']:
            Vpcs.append( [{ 'VpcId': i['VpcId'], 'CidrBlock': i['CidrBlock'], 'Name': j['Value']}] )
    return Vpcs

def GetAccoundId():
    AccountId = boto3.client('sts').get_caller_identity()['Account']
    return AccountId 

def GetInstanceId(InstanceName):
    client = GetClient(Service = Service, Region = Region, Profile = Profile)
    response = None  
    try:
        response = client.describe_instances(
            Filters = [
                {
                    'Name': 'tag-value',
                    'Values': [InstanceName, ]
                }
            ]
        )
    except Exception as e:
        print(e)

    for r in response['Reservations']:
        for s in r['Instances']:
#            print(s['InstanceId'])
            for t in s['State']:
                for v in t['Name']:
                    print(v)

# -- Get Role Name -- # 
def GetRole(Service = 'iam', Profile = 'default' , RoleName = 'Ec2Role' ):
    client = GetClient(Service = Service, Region = Region, Profile = Profile)
    response = None 
    try:
        response = client.get_role(
            RoleName = RoleName
        )
    except Exception as e:
        print(e)

    return response

def GetRegion():
    return boto3.session.Session().region_name or 'us-east-1'

def GetAccountId():
    return boto3.resource('iam').CurrentUser().arn.split(':')[4]

# -- Get a Internet Gateway Id of specific VpcId-- # 
def GetInternetGateway(VpcId):
    client = GetClient(Service, Region, Profile)

    response = client.describe_internet_gateways()['InternetGateways']
    for res in response:
        for r in res['Attachments']:
            if r['VpcId'] == VpcId:
                return res['InternetGatewayId']

    return None

# -- Get subnets of specific VpcId -- # 
def GetSubnets(VpcId):
    client = GetClient(Service, Region, Profile)

    response = client.describe_subnets(
        Filters = [
            {
                'Name':'vpc-id',
                'Values': [VpcId, ],
            }
        ]
    )['Subnets']
    return response


# -- Get Network Acls of specific VpcId -- # 
def GetNetworkAcls(VpcId):
    Nacls = None 
    client = GetClient(Service, Region, Profile)

    response = client.describe_network_acls(
        Filters = [
            {
                'Name':'vpc-id',
                'Values': [VpcId, ],
            }
        ]
    )['NetworkAcls']
    return response

# -- Get Security Groups of specific VpcId -- # 
def GetSecurityGroups(VpcId):
    client = GetClient(Service, Region, Profile)

    response = client.describe_security_groups(
        Filters = [
            {
                'Name':'vpc-id',
                'Values': [VpcId, ],
            }
        ]
    )['SecurityGroups']
    return response

# -- Get Routing Tables of specific VpcId -- # 
def GetRouteTables(VpcId):
    client = GetClient(Service, Region, Profile)

    response = client.describe_route_tables(
        Filters = [
            {
                'Name':'vpc-id',
                'Values': [VpcId, ],
            }
        ]
    )['RouteTables']
    return response

# -- Get Elastic Ip Addresses -- # 
def GetElasticIpAddresses():
    client = GetClient(Service, Region, Profile)

    response = client.describe_addresses()['Addresses']
    return response

# -- Release Elastic Ip Addresses -- # 
def ReleaseAddress(AllocationId):
    client = GetClient(Service, Region, Profile)

    response = client.release_address(AllocationId = AllocationId)
    return response

def CreateSnsTopic(Service, Name): 
    client = GetClient(Service, Region, Profile)
    response = client.create_topic(Name = Name)
    return response

def CreateSubscription(TopicArn):

    client = GetClient('sns', Region, Profile) 
    response = client.subscribe(
        TopicArn = TopicArn,
        Protocol = 'email',
        Endpoint = 'liverpools@gmail.com',
        ReturnSubscriptionArn = True
    )
    return response
