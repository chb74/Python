# -- By liverpools@gmail.com -- # 
# -- On Jan 2, 2022 -- # 

import boto3, logging, time, datetime, json , os, sys, pprint 
from Libs import GetClient, CreateTags, GetIdFromTag

# -- boto3.set_stream_logger('boto3', logging.DEBUG)

Vpcs = {
    "ProjectPrefix": "Chb-Dev",
    "VpcCidr": "10.70.0.0/16",
    "VpcId": "vpc-01815c1dd30f6db6c",

    "Service": "ec2",
    "Profile": "default",
    "Region": "ap-northeast-2",

    "InstanceTenancy": "default",
    "UseKeyPair": 0,
    "UseNatGateway": 0,
    "AZ1": "ap-northeast-2a",
    "AZ2": "ap-northeast-2b",
    "AZ3": "ap-northeast-2c",
    "AZ4": "ap-northeast-2d",
    # -- Define Tags -- # 
    "VpcTag": "-VPC",
    "InternetGatewayTag": "-IGW",
    "SubnetTag": "-SN-",
    "SecurityGroupTag": "-SG-",
    "NetworkAclTag": "-NACL-",
    "RouteTableTag": "-RT-",
    "EipTag": "-EIP-",
    "EniTag": "-ENI-",
    "EndPointTag": "-EP-",
    "EndPointServiceTag": "-EPS-",
    "CustomerGatewayTag": "-CGW-",
    "VirtualGateway": "-VGW-",
    "VolumeTag": "-VOL-",
    "NetworkInterfaceTag": "-ENI-",
    "ElbTag": "-ELB-",
    "TargetGroupTag": "-TG-",

    "SecurityGroups": [
        "Bastion", "Web", "Was", "App", "Db", "Cache", "Glue", "RedShift", "Was-Ext-Elb", "Web-Ext-Elb", "Eks-Cluster", "Eks-CP", "Eks-Workers", "Ecs-Web", "Ecs-Was", "Was-Int-Elb", "Web-Int-Elb"
    ],
    "Instances": [
        {
            "InstanceName": "Web-A", 
            "AmiId": "ami-05ca8403ef4546dac",
            "KeyPair": "chb-seoul", 
            "InstanceType": "t4g.medium", 
            "Subnet": "Pub-A", 
            "SecurityGroup": "Web", 
            "DeleteOnTermination": True, 
            "DisableApiTermination": True, 
            "VolumeType": "gp2",
            "VolumeSize": 20,
            "PrivateIpAddress": "10.70.0.10",
            "Eip": True
        },
        {
            "InstanceName": "Web-C", 
            "AmiId": "ami-05ca8403ef4546dac",
            "KeyPair": "chb-seoul", 
            "InstanceType": "t4g.medium", 
            "Subnet": "Pub-C", 
            "SecurityGroup": "Web", 
            "DeleteOnTermination": True, 
            "DisableApiTermination": True, 
            "VolumeType": "gp2",
            "VolumeSize": 20,
            "PrivateIpAddress": "10.70.1.10",
            "Eip": True
        },
    ],
    "Subnets": [
        {
        "Pub-A": "10.70.0.0/24",
        "Pub-C": "10.70.1.0/24",
        "Priv-A": "10.70.2.0/24",
        "Priv-C": "10.70.3.0/24",
        "Db-A": "10.70.4.0/24",
        "Db-C": "10.70.5.0/24",
        "Sec-A": "10.70.10.0/24",
        "Sec-C": "10.70.11.0/24"
        },
    ],
    "Elbs": [
        {
            "Service": "elbv2",
            "Elb": [
                {
                    "ElbName": "Alb-Web-Ext",
                    "Subnets": [ "Pub-A", "Pub-C"],
                    "SecurityGroups": [ "Web-Ext-Elb"],
                    "Scheme": "internet-facing",
                    "Type": "application",
                    "IpAddressType": 'ipv4',

                    # -- Target Group -- # 
                    "TargetGroupName": "Alb-Web-Ext-80",
                    "Protocol": "HTTP",
                    "ProtocolVersion": "HTTP1",
                    "Port": 80, 
                    "HealthCheckProtocol": "HTTP",
                    "HealthCheckPort": "80",
                    "HealthCheckEnabled": True,
                    #"HealthCheckPath": '/',
                    "HealthCheckIntervalSeconds": 10,
                    "HealthCheckTimeoutSeconds": 5,
                    "HealthyThresholdCount": 3,
                    "UnhealthyThresholdCount": 3, 
                    "TargetType": "instance",
                },
                {
                    "ElbName": "Nlb-Web-Ext",
                    "Subnets": [ "Pub-A", "Pub-C"],
                    "Scheme": "internet-facing",
                    "Type": "network",
                    "IpAddressType": 'ipv4',

                    # -- Target Group -- # 
                    "TargetGroupName": "Nlb-Ext-80",
                    "Protocol": "TCP",
                    "ProtocolVersion": "TCP",
                    "Port": 80, 
                    "HealthCheckProtocol": "TCP",
                    "HealthCheckPort": "80",
                    "HealthCheckEnabled": True,
                    "HealthCheckIntervalSeconds": 10,
                    "HealthCheckTimeoutSeconds": 5,
                    "HealthyThresholdCount": 3,
                    "UnhealthyThresholdCount": 3, 
                    "TargetType": "ip",
                },
            ]
        }
    ],
}

Tags = {
    "Backup-Retention": 7,
    "AutoStop": "No",
    "AutoStart": "No",
    "Env": "Production",
}

# -- Create a Vpc -- # 
def CreateVpc(**Params):
    client = GetClient(Params["Service"], Params["Region"], Params["Profile"])

    VpcName = f"{Params['ProjectPrefix']}{Params['VpcTag']}"
    response = client.create_vpc(
        CidrBlock = Params['VpcCidr'],
        DryRun = False,
        InstanceTenancy = Params['InstanceTenancy'],
        TagSpecifications = [
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': VpcName
                    },
                    {
                        'Key': 'Environment',
                        'Value': 'Production'
                    },
                    {
                        'Key': 'Priority',
                        'Value': '1'
                    },
                ]
            }
        ]
    )
    return response['Vpc']['VpcId']

# -- Create a subnets -- # 
def CreateSubnet(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
    response = None 
    Count = 0

    for sn in Params["Subnets"]:
        for s, i in sn.items():
            # -- 2 AZ use -- # 
            if (Count % 2) == 0: 
                AZ = Params['AZ1']
            else:
                AZ = Params['AZ3']

            SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{s}"
            response = client.create_subnet(
                TagSpecifications = [
                    {
                        'ResourceType': 'subnet',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': SubnetName
                            }
                        ]
                    }
                ],
                AvailabilityZone = AZ,
                CidrBlock = i,
                VpcId = Params['VpcId'],
                DryRun = False
            )
            Count += 1
    return response

# -- Create a Route Tables -- # 
def CreateRouteTables(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for rt in Params['Subnets']:
        for r, i in rt.items():
            RouteTableName = f"{Params['ProjectPrefix']}{Params['RouteTableTag']}{r}"
            SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{r}"
            RouteTableId = None 
            # -- def GetIdFromTag(Object, Tag, VpcId, **Params): 
            SubnetId = GetIdFromTag("sn", SubnetName, **Params)
            try:
                response = client.create_route_table(
                    DryRun = False,
                    VpcId = Params['VpcId'],
                    TagSpecifications = [
                        {
                            'ResourceType': 'route-table',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': RouteTableName
                                }
                            ]
                        }
                    ]
                )
                RouteTableId = response['RouteTable']['RouteTableId']
            except Exception as e:
                print(e)

# -- Create a Internet Gateway -- # 
def CreateInternetGateway(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    InternetGatewayName = f"{Params['ProjectPrefix']}{Params['InternetGatewayTag']}"
    response = client.create_internet_gateway(
        TagSpecifications = [
            {
                'ResourceType': 'internet-gateway',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': InternetGatewayName
                    }
                ]
            }
        ]
    )
    IgwId = response['InternetGateway']['InternetGatewayId']
    response = client.attach_internet_gateway(
        InternetGatewayId = IgwId, 
        VpcId = Params['VpcId'],
    )
    return IgwId

# -- Create a Security Group -- # 
def CreateSecurityGroups(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for i in Params['SecurityGroups']:
        SecurityGroupName = f"{Params['ProjectPrefix']}{Params['SecurityGroupTag']}{i}"

        response = client.create_security_group(
            Description = SecurityGroupName,
            GroupName = SecurityGroupName,
            VpcId = Params['VpcId'],
            TagSpecifications = [ 
                { 
                    'ResourceType': 'security-group',
                    'Tags': [ 
                        { 
                            'Key': 'Name',
                            'Value': SecurityGroupName
                        }
                    ]
                }
            ],
            DryRun = False
        )

# -- Create a Network ACL -- # 
def CreateNetworkACL(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for i in Params['Subnets']:
        for k,_ in i.items():
            NetworkAclName = f"{Params['ProjectPrefix']}{Params['NetworkAclTag']}{k}"
            SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{k}"
            SubnetId = GetIdFromTag("sn", SubnetName, **Params)

            response = client.create_network_acl(
                DryRun = False,
                VpcId = Params['VpcId'],
                TagSpecifications = [ 
                    {
                        'ResourceType': 'network-acl',
                        'Tags': [ 
                            {
                                'Key': 'Name',
                                'Value': NetworkAclName
                            }
                        ]
                    }
                ]
            )

            NetworkAclId = response['NetworkAcl']['NetworkAclId']

            res = client.create_network_acl_entry( 
                CidrBlock = '0.0.0.0/0',
                DryRun = False,
                Egress = True,
                NetworkAclId = NetworkAclId,
                Protocol = '-1',
                RuleAction = 'allow',
                RuleNumber = 100
            )
            res = client.create_network_acl_entry(
                CidrBlock = '0.0.0.0/0',
                Egress = False,
                NetworkAclId = NetworkAclId,
                Protocol = '-1',
                RuleAction = 'allow',
                RuleNumber = 100
            )

            AssociatedId = GetAssociationId(SubnetId, **Params)

            try:
                response = client.replace_network_acl_association(
                    AssociationId = AssociatedId, 
                    NetworkAclId = NetworkAclId 
                )
            except Exception as e:
                print(e)

# -- Get Network Acls Association ID -- # 
def GetAssociationId(SubnetId, **Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
    response = None 
    try:
        response = client.describe_network_acls()
    except Exception as e:
        print(e)
    AssociateId = None 
    for i in response['NetworkAcls']:
        for j in i['Associations']:
            if j['SubnetId'] == SubnetId:
                AssociateId = j['NetworkAclAssociationId']
    return AssociateId

# -- Associate Route Tables Rules -- # 
def AssociateRouteTable(**Params): 
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for i in Params['Subnets']:
        for k,_ in i.items():
            RouteTableName = f"{Params['ProjectPrefix']}{Params['RouteTableTag']}{k}"
            SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{k}"
            RouteTableId = GetIdFromTag("rt", RouteTableName, **Params)
            SubnetId = GetIdFromTag("sn", SubnetName, **Params)
            response = client.associate_route_table(
                DryRun = False,
                RouteTableId = RouteTableId,
                SubnetId = SubnetId,
            )

# -- Create a Route Configure -- # 
def CreateRoute(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for i in Params['Subnets']:
        for k,_ in i.items():
            if "pub" not in k.lower():
                continue
            else:
                RouteTableName = f"{Params['ProjectPrefix']}{Params['RouteTableTag']}{k}"
                RouteTableId = GetIdFromTag("rt", RouteTableName, **Params)
                InternetGatewayName = f"{Params['ProjectPrefix']}{Params['InternetGatewayTag']}"
                InternetGatewayId = GetIdFromTag("igw", InternetGatewayName, **Params)

                response = client.create_route(
                    DestinationCidrBlock = "0.0.0.0/0",
                    DryRun = False,
                    GatewayId = InternetGatewayId,
                    RouteTableId = RouteTableId,
                )

# -- Create a EC2 Instances -- # 
def CreateInstances(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])
    InstanceId = None 
    VolumeId = None 
    EniId = None 

    for j in Params['Instances']:
        InstName = f"{Params['ProjectPrefix']}-{j['InstanceName']}"
        SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{j['Subnet']}"
        SubnetId = GetIdFromTag("sn", SubnetName, **Params)
        SecurityGroupName = f"{Params['ProjectPrefix']}{Params['SecurityGroupTag']}{j['SecurityGroup']}"
        SecurityGroupId = GetIdFromTag("sg", SecurityGroupName, **Params)
        VolumeName = f"{Params['ProjectPrefix']}{Params['VolumeTag']}{j['InstanceName']}"
        EniName = f"{Params['ProjectPrefix']}{Params['EniTag']}{j['InstanceName']}"
        DeviceName = None 

        response = client.run_instances(
            BlockDeviceMappings = [ 
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': j['VolumeSize'],
                        'VolumeType': j['VolumeType'],
                        'Encrypted': True,
                    }
                }
            ],
            ImageId = j['AmiId'],
            InstanceType = j['InstanceType'],
            KeyName = j['KeyPair'],
            MaxCount = 1,
            MinCount = 1,
            Monitoring = {
                'Enabled': True
            },
            SecurityGroupIds = [ SecurityGroupId ],
            SubnetId = SubnetId,
            DisableApiTermination = j['DisableApiTermination'], 
            DryRun = False,
            TagSpecifications = [ 
                { 
                    'ResourceType': 'instance',
                    'Tags': [ 
                        {
                            'Key': 'Name',
                            'Value': InstName
                        }
                    ]
                }
            ],
            PrivateIpAddress = j['PrivateIpAddress'],
        )
        for inst in response['Instances']:
            InstanceId = inst['InstanceId']
            for ni in inst['NetworkInterfaces']:
                EniId = ni['NetworkInterfaceId']

        waiter = client.get_waiter('instance_running')
        waiter.wait(InstanceIds = [InstanceId])

        if j['Eip']:
            EipName = f"{Params['ProjectPrefix']}{Params['EipTag']}{j['InstanceName']}"

            response = client.allocate_address(
                TagSpecifications=[
                    {
                        'ResourceType': 'elastic-ip',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': EipName
                            },
                        ]
                    },
                ]
            )
            AllocationId = response['AllocationId']

            response = client.associate_address(
                AllocationId = AllocationId,
                InstanceId = InstanceId
            )
        else:
            pass

        # -- Get VolumeId And Tagging to volume -- # 
        res = client.describe_instances( InstanceIds = [ InstanceId])
        for inst in res['Reservations']:
            for i in inst['Instances']:
                for j in i['BlockDeviceMappings']:
                    VolumeId = j['Ebs']['VolumeId']
                    DeviceName = j['DeviceName']
                    Volume = f"{VolumeName}:{DeviceName}"
                    CreateTags(VolumeId, Volume, "Name", **Params)

        # -- Tagging to ENI -- # 
        CreateTags(EniId, EniName, "Name", **Params)

# -- Create a Elb -- # 
def CreateElb(**Params):

    for elb in Params['Elbs']:
        client = GetClient(elb['Service'], Params['Region'], Params['Profile'])
        for e in elb['Elb']:
            LoadBalancerName = f"{Params['ProjectPrefix']}{Params['ElbTag']}{e['ElbName']}"
            Subnets = []
            SecurityGroups = []

            for sb in e['Subnets']:
                SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{sb}"
                i = GetIdFromTag("sn", SubnetName, **Params)
                Subnets.append(i)
            if e['Type'] == "network":
                pass
            else:
                for sg in e['SecurityGroups']:
                    SecurityGroupName = f"{Params['ProjectPrefix']}{Params['SecurityGroupTag']}{sg}"
                    i = GetIdFromTag("sg", SecurityGroupName, **Params)
                    SecurityGroups.append(i)

            response = client.create_load_balancer(
                Name = LoadBalancerName, 
                Subnets = Subnets,
                SecurityGroups = SecurityGroups,
                Scheme = e['Scheme'],
                Tags = [ 
                    {
                        'Key': 'Name',
                        'Value': LoadBalancerName,
                    }
                ],
                Type = e['Type'],
                IpAddressType = e['IpAddressType']
            )
            LbArn = None 
            for i in response['LoadBalancers']:
                e['LoadBalancerArn'] = i['LoadBalancerArn']
            CreateTargetGroup(**e)

# -- Create a Listner -- # 
def CreateListener(**Params):
    client = GetClient("elbv2", Vpcs['Region'], Vpcs['Profile'])

    ListenerName = f"{Params['ElbName']}-{Params['Port']}"
    response = client.create_listener(
        LoadBalancerArn = Params['LoadBalancerArn'],
        Protocol = Params['Protocol'],
        Port = Params['Port'],
        DefaultActions = [
            {
                'Type': 'forward',
                'TargetGroupArn': Params['TargetGroupArn'],
            }
        ]
    )
# -- Create a Target Group -- # 
def CreateTargetGroup(**Params):

    client = GetClient("elbv2", Vpcs['Region'], Vpcs['Profile'])

    TargetGroupName = f"{Vpcs['ProjectPrefix']}{Vpcs['TargetGroupTag']}{Params['TargetGroupName']}"

    response = client.create_target_group(
        Name = TargetGroupName, 
        Protocol = Params['Protocol'],
        #ProtocolVersion = Params['ProtocolVersion'],
        Port = Params['Port'],
        VpcId = Vpcs['VpcId'],
        HealthCheckProtocol = Params['HealthCheckProtocol'],
        HealthCheckPort = Params['HealthCheckPort'],
        HealthCheckEnabled = Params['HealthCheckEnabled'],
        HealthCheckIntervalSeconds = Params['HealthCheckIntervalSeconds'],
        #HealthCheckTimeoutSeconds = Params['HealthCheckTimeoutSeconds'],
        HealthyThresholdCount = Params['HealthyThresholdCount'],
        UnhealthyThresholdCount = Params['UnhealthyThresholdCount'],
        TargetType = Params['TargetType'],
        Tags = [
            {
                'Key': 'Name',
                'Value': TargetGroupName 
            }
        ],
        IpAddressType = 'ipv4'
    )
    for i in response['TargetGroups']:
        Params['TargetGroupArn'] = i['TargetGroupArn'] 
    CreateListener(**Params)



# -- Main Function -- # 
if __name__=="__main__":
    BeginTime = time.time()
    """
    VpcId = CreateVpc(**Vpcs)
    Vpcs['VpcId'] = VpcId 

    res = CreateSubnet(**Vpcs)
    res = CreateRouteTables(**Vpcs)
    res = CreateInternetGateway(**Vpcs)
    res = CreateSecurityGroups(**Vpcs)
    res = CreateNetworkACL(**Vpcs)
    res = AssociateRouteTable(**Vpcs)
    res = CreateRoute(**Vpcs)
    res = CreateInstances(**Vpcs)
    """
    res = CreateElb(**Vpcs)

    print(" * -- Tasks took %3.3f Seconds -- *" % (time.time() - BeginTime))