# -- by chb -- #
# -- on Mar 9, 2021 -- #

import boto3, time

Service = 'ec2'

# -- Attach the Tags -- #
def CreateTags(**Params):
    client = boto3.client(Service)
    response = client.create_tags(
        DryRun = False,
        Resources = [
            Params['Resource']
        ],
        Tags=[
            {
                'Key': Params['Key'],
                'Value': Params['Value']
            },
        ]
    )

# -- Creating Amazon Machine Image -- #
def CreateAmi(**Params):
    response = None
    client = boto3.client(Service)
    try:
        response = client.create_image(
            InstanceId = Params['InstanceId'],
            Name = Params['AmiName'],
            NoReboot = Params['NoReboot'],
            Description = Params['Description'],
        )
    except Exception as e:
        print(e)
    return response['ImageId']

# -- Creating Launch Template -- #
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

# -- Create Auto Scaling Group -- #
def CreateAutoScaleGroup(**Params):
    Service = 'autoscaling'
    client = boto3.client(Service)

    try:
        response = client.create_auto_scaling_group(
            AutoScalingGroupName = Params['AutoScalingGroupName'],
            LaunchTemplate = {
                'LaunchTemplateId': '',
                'LaunchTemplateName': '',
                'Version': ''
            },
            MinSize = Params['MinSize'],
            MaxSize = Params['MaxSize'],
            DesiredCapacity = Params['DesiredCapacity'],
            DefaultCooldown = Params['DefaultCooldown'],
            AvailabilityZones = Params['AvailabilityZones'],
            LoadBalancerNames = Params['LoadBalancerNames'],
            TargetGroupARNs = Params['TargetGroupARNs'],
            TerminationPolicies = Params['TerminationPolicies'],
            HealthCheckType = Params['HealthCheckType'],
            HealthCheckGracePeriod = Params['HealthCheckGracePeriod'],
            VPCZoneIdentifier = Params['VPCZoneIdentifier'],
            Tags = Params['Tags']
        )
    except Exception as e:
        print(e)

    return response

# -- Main Routine -- #
if __name__=="__main__":
    Asg = {
        'AutoScalingGroupName': 'Chb-Asg-Web',
        'LaunchConfigurationName': ,
        'MinSize': 0,
        'MaxSize': 10,
        'DesiredCapacity': 0,
        'DefaultCooldown': 360,
        'AvailabilityZones': 'ap-northeast-2a,ap-northeast-2c',
        'LoadBalancerNames': 'Chb-Web',
        'TargetGroupARNs': '',
        'TerminationPolicies': '',
        'HealthCheckType': '',
        'HealthCheckGracePeriod': 10,
        'VPCZoneIdentifier': '',
        'Tags': [],
    }
    res = CreateAutoScaleGroup(**Asg)
    print(res)
"""
    first = time.time()
    AmiName = 'Chb-Web-' + str(int(time.time()))

    # -- Create a Image -- #
    Image = { 'InstanceId': 'i-03e8fca9dd011b43d', 'AmiName': AmiName, 'NoReboot': True, 'Description': 'Web Server' }
    ImageId = CreateAmi(**Image)

    available = 0
    client = boto3.client(Service)

    # -- -- #
    while available == 0:
        response = client.describe_images(
            ImageIds = [ ImageId, ]
        )['Images']
        for res in response:
            if res['State'] == 'available':
                available = 1
            else:
                pass

    Tags = {'Resource': ImageId, 'Key': 'Name', 'Value': 'Chb-Web'}
    CreateTags(**Tags)

    LaunchTemplate = {
        'LaunchTemplateName': 'Chb-Web-LaunchTemplate',
        'VersionDescription': '1.0',
        'IamInstanceProfile': 'arn:aws:iam::619663388442:instance-profile/Chb-Ec2-Instance-Profile',
        'InstanceProfileName': 'Chb-Ec2-Instance-Profile',
        'DeviceName': '/dev/xvda',
        'Encrypted': True,
        'DeleteOnTermination': True,
        'VolumeSize': 50,
        'VolumeType': 'gp2',
        'ImageId': 'ami-006e2f9fa7597680a',
        'InstanceType': 't3a.medium',
        'KeyName': 'chb-seoul',
        'MonitoringEnabled':True,
        'SecurityGroupIds': 'sg-02d2c6745014fbb9b',
    }

    res = CreateLaunchTemplate(**LaunchTemplate)
    LaunchTemplateId = res['LaunchTemplate']['LaunchTemplateId']

    print(" * It takes time : %3.1f seconds" % (time.time() - first))
"""%