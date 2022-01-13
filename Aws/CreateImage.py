# -- By Chb 
# -- On Jan 13, 2022 

import boto3, sys, datetime, time

CurrentDate = datetime.date.today()
CurrentDate = CurrentDate.strftime('%m%d')

# -- Define Environment Variables -- # 
Params = { 
    "Service": "ec2",
    "Region": "ap-northeast-2", 
    "Profile": "meritz",
    "InstId": "i-01b38952eba64c536",
    "InstName": f"Meritz-PoC-Bastion-{CurrentDate}",
    "VpcId": "vpc-0f684a9333082ee83",

    "InstanceName": "Web-A", 
    "AmiId": "ami-05ca8403ef4546dac",
    "KeyPair": "chb-seoul", 
    "InstanceType": "t4g.medium", 
    "Subnet": "Pub-A", 
    "SecurityGroup": "Web", 
    "DeleteOnTermination": True, 
    "DisableApiTermination": True, 

    # -- Launch Template -- # 
    'LaunchTemplateName': 'Meritz-PoC-LT-MCI',
    'VersionDescription': '1.0',
    'IamInstanceProfile': '',
    'InstanceProfileName': 'Chb-Ec2-Instance-Profile',
    'Encrypted': True,
    'DeleteOnTermination': True,
    'ImageId': 'ami-006e2f9fa7597680a',
    'InstanceType': 't3a.medium',
    'KeyName': 'Meritz-PoC-seoul',
    'MonitoringEnabled':True,
    'SecurityGroupIds': 'sg-02d2c6745014fbb9b',
}

# -- GetClient -- # 
def GetClient(Service = 'ec2', Region = 'ap-northeast-2', Profile = 'default'):
    session = boto3.Session(profile_name = Profile)
    client = session.client(Service, Region)
    return client 


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


def CreateInstance(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    response = client.run_instances(


    )

    return InstanceId 
# -- Create a Images -- # 
def CreateImage(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    response = client.create_image(
        InstanceId = Params['InstId'],
        Name = Params['InstName'], 
        Description = Params['InstName'],
        NoReboot = True,
        TagSpecifications = [
            {
                'ResourceType': 'image',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Params['InstName']
                    }, 
                    {
                        'Key': 'Env',
                        'Value': 'PoC'
                    }
                ]
            }
        ]
    )

    ImageId  = response['ImageId']

    waiter = client.get_waiter('image_available')
    waiter.wait(ImageIds = [ImageId])
    return ImageId

# -- Get Image status -- # 
def GetImageStat(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
    response  = client.describe_images(
        ImageIds = [Params['ImageId']],
    )

    for i in response['Images']:
        print(i['State'])

# -- Create Launch Template -- # 
def CreateLaunchTemplate(**Params):
    client = boto3.client(Service)

    response = client.create_launch_template(
        DryRun = False,
        LaunchTemplateName = Params['LaunchTemplateName'],
        VersionDescription = Params['VersionDescription'],
        LaunchTemplateData = {
            'IamInstanceProfile': {
                'Arn': Params['IamInstanceProfile'],
                'Name': Params['InstanceProfileName'],
            },
            'BlockDeviceMappings': [
                {
                    'DeviceName': Params['DeviceName'],
                    'Ebs': {
                        'Encrypted': Params['Encrypted'],
                        'DeleteOnTermination': Params['DeleteOnTermination'],
                        'VolumeSize': Params['VolumeSize'],
                        'VolumeType': Params['VolumeType'],
                    },
                },
            ],
            'ImageId': Params['ImageId'],
            'InstanceType': Params['InstanceType'],
            'KeyName': Params['KeyName'],
            'Monitoring': { 'Enabled': Params['MonitoringEnabled'] },
            'SecurityGroupIds': [ Params['SecurityGroupIds'], ],
        }
    )

    return response

if __name__=="__main__":
    BeginTime = time.time()

    ImageId = CreateImage(**Params)

    Params['ImageId'] = ImageId
    GetImageStat(**Params)

    print("Finished creating Image : %s" % (ImageId))
    print("It took time %3.3f" % (time.time() - BeginTime))