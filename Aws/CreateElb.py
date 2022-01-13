# -- By liverpools@gmail.com -- # 
# -- On Jan 2, 2022 -- # 

import boto3, logging, time, datetime, json , os, sys 
from Libs import GetClient, CreateTags, GetIdFromTag

# -- boto3.set_stream_logger('boto3', logging.DEBUG)


Vpcs = {
    "ProjectPrefix": "Chb-Dev",
    "VpcCidr": "10.70.0.0/16",

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

    "SecurityGroups": [
        "Bastion", "Web", "Was", "Db", "Cache", "Glue", "RedShift", "Was-Elb", "Web-Elb"
    ],
    "Instances": [
        {
            "InstanceName": "Bastion-A", 
            "AmiId": "ami-05ca8403ef4546dac",
            "KeyPair": "chb-seoul", 
            "InstanceType": "t4g.medium", 
            "Subnet": "Pub-A", 
            "SecurityGroup": "Bastion", 
            "DeleteOnTermination": True, 
            "DisableApiTermination": False, 
            "VolumeType": "gp2",
            "VolumeSize": 50,
            "PrivateIpAddress": "10.70.0.10",
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
        "Sec-A": "10.70.6.0/24",
        "Sec-C": "10.70.7.0/24"
        },
    ],
    Elbs = [
        {
            "Service": "elbv2",

            "ElbTag": "-ELB-",
            "TargetGroupTag": "-TG-",
            "SubnetTag": "-SN-",
            "SecurityGroupTag": "-SG-",

            "Elb": [
                {
                    "ElbName": "Web-Ext",
                    "Subnets": [ "Pub-A", "Pub-C"],
                    "SecurityGroups": [ "Web-Elb"],
                    "Scheme": "internet-facing",
                    "Type": "application",
                    "IpAddressType": 'ipv4',

                    # -- Target Group -- # 
                    "TargetGroupName": "Web-Ext-80",
                    "Protocol": "HTTP",
                    "ProtocolVersion": "HTTP1",
                    "Port": 80, 
                    "HealthCheckProtocol": "HTTP",
                    "HealthCheckPort": "80",
                    "HealthCheckEnabled": True,
                    "HealthCheckPath": '/',
                    "HealthCheckIntervalSeconds": 10,
                    "HealthCheckTimeoutSeconds": 5,
                    "HealthyThresholdCount": 3,
                    "UnhealthyThresholdCount": 5, 
                    "TargetType": "instance",
                },
            ]
        }
    ],
}

BeginTime = time.time()

def CreateElb(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    for elb in Params['Elb']:
        ElbName = f"{Params['ProjectPrefix']}{Params['ElbTag']}{elb['ElbName']}"
        Subnets = []
        SecurityGroups = []

        for sb in elb['Subnets']:
            SubnetName = f"{Params['ProjectPrefix']}{Params['SubnetTag']}{sb}"
            i = GetIdFromTag("sn", SubnetName, **Params)
            Subnets.append(i)

        for sg in elb['SecurityGroups']:
            SecurityGroupName = f"{Params['ProjectPrefix']}{Params['SecurityGroupTag']}{sg}"
            i = GetIdFromTag("sg", SecurityGroupName, **Params)
            SecurityGroups.append(i)

        response = client.create_load_balancer(
            Name = ElbName, 
            Subnets = Subnets,
            SecurityGroups = SecurityGroups,
            Scheme = elb['Scheme'],
            Tags = [ 
                {
                    'Key': 'Name',
                    'Value': ElbName,
                }
            ],
            Type = elb['Type'],
            IpAddressType = elb['IpAddressType']
        )
        print(response)


def CreateTargetGroup(**Params):
    client = GetClient(Params['Service'], Params['Region'], Params['Profile'])

    TargetGroupName = f"{Params['ProjectPrefix']}{Params['TargetGroupTag']}{Params['TargetGroupName']}"

    response = client.create_target_group(
        Name = TargetGroupName, 
        Protocol = Params['Protocol'],
        ProtocolVersion = Params['ProtocolVersion'],
        Port = Params['Port'],
        VpcId = Params['VpcId'],
        HealthCheckProtocol = Params['HealthCheckProtocol'],
        HealthCheckPort = Params['HealthCheckPort'],
        HealthCheckEnabled = Params['HealthCheckEnabled'],
        HealthCheckPath = Params['HealthCheckPath'],
        HealthCheckIntervalSeconds = Params['HealthCheckIntervalSeconds'],
        HealthCheckTimeoutSeconds = Params['HealthCheckTimeoutSeconds'],
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
    return response

# -- Start Creation -- # 
res = CreateElb(**Elbs)
#res = CreateTargetGroup(**Elbs)
print(res)

print(" * -- Tasks took %3.3f Seconds -- *" % (time.time() - BeginTime))
