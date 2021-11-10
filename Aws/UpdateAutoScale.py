# -- On Nov 22, 2017  -- # 
# -- By liverpools@gmail.com  -- # 
# -- AutoScaleAllInOne : Create a AMI -> Launch Configuration -> Create a Auto Scale Group

import boto3, json, time, sys, re, logging

Instances = {}
AmiId = ''
CreateAsg = False

# -- boto3.set_stream_logger('boto3', logging.DEBUG)
Instance = { 
    'InstanceName': 'Prd-Web-Lnx-001', 
    'AlbName': 'Prod-Poc-Elb',
    'AsgName': 'Prd-Web-Asg',
}

LcInfo = {
    'LaunchConfigurationName': 'Mz_Lc-Latest',
    'KeyName': 'chbaek',
    'InstanceType': 'c4.large',
    'InstanceMonitoring': {'Enabled': False},
    'SpotPrice': '0.3',
    'AssociatePublicIpAddress': False
}

AsgInfo = {
      'AutoScalingGroupName' : 'Prod-Web-Asg',
      'LaunchConfigurationName' : LcInfo['LaunchConfigurationName'],
      'MinSize' : 0,
      'MaxSize' : 10,
      'DesiredCapacity' : 0,
      'DefaultCooldown' : 300,
      'AvailabilityZones': ['ap-northeast-2a', 'ap-northeast-2c'],
      'TerminationPolicies': [ 'OldestInstance', ],
      'HealthCheckType' : 'EC2',
      'HealthCheckGracePeriod': 300,
      'VPCZoneIdentifier': 'subnet-xxx,subnet-xxx',
      'Tags' : [ { 'Key' : 'Name', 'Value': Instance['AsgName'] }]
}

# -- This is a Session for AWS Connection -- # 
def GetClient(Service = 'ec2', Region = Region, Profile = Profile):
    session = boto3.Session(profile_name = Profile)
    client = session.client(Service, Region)
    
    return client

# -- This Function creates Tags about Resource -- #
def CreateTags(Resource, Values, Key = "Name"):
    time.sleep(0.2)
    client = GetClient("ec2")
    Tags = {}
    try:
        Tags = client.create_tags(
            Resources = [ Resource ],
            Tags=[{'Key':Key, 'Value': Values}]
        )
    except Exception as e:
        print(e)
    return Tags


# -- Create a Ami of specific Instance -- # 
def CreateAmi(**Params):
    client = GetClient()
    response = {}

    try:
        response = client.create_image(
            InstanceId = Params['InstanceId'],
            Name = Params['AmiName'], 
            NoReboot = True,
        )
    except Exception as e:
        print(e)
    return response 

# -- Create a launch Configuration -- # 
def CreateLaunchConfiguration(**Params):
    client = GetClient("autoscaling")
    response = None 

    response = client.describe_launch_configurations()

    for l in response['LaunchConfigurations']:
        if l['LaunchConfigurationName'] == Params['LaunchConfigurationName']:
            import uuid
            string = uuid.uuid4().hex
            Params['LaunchConfigurationName'] += "-" + string[0:8]
            LcInfo['LaunchConfigurationName'] += "-" + string[0:8]
            AsgInfo['LaunchConfigurationName'] += "-" + string[0:8]
        else: 
            pass
    try:
        response = client.create_launch_configuration( 
            LaunchConfigurationName = Params['LaunchConfigurationName'],
            ImageId = Params['ImageId'], 
            KeyName = Params['KeyName'], 
            SecurityGroups = Params['SecurityGroups'],
            InstanceType = Params['InstanceType'] ,
            InstanceMonitoring = Params['InstanceMonitoring'],
            # -- SpotPrice = Params['SpotPrice'],
            AssociatePublicIpAddress = Params['AssociatePublicIpAddress']
        )
    except Exception as e:
        print(e)
    return response 

# -- Create a auto scaling group -- # 
def CreateAutoScalingGroup(**Params):
    client = GetClient("autoscaling")
    response = {}

    try:
        response = client.create_auto_scaling_group(
            AutoScalingGroupName = Params['AutoScalingGroupName'],
            LaunchConfigurationName = Params['LaunchConfigurationName'],
            MinSize = Params['MinSize'],
            MaxSize = Params['MaxSize'],
            DesiredCapacity = Params['DesiredCapacity'],
            DefaultCooldown = Params['DefaultCooldown'],
            AvailabilityZones = Params['AvailabilityZones'],
            # -- LoadBalancerNames = Params['LoadBalancerNames'],
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

def UpdateAutoScalingGroup(**Params):
    client = GetClient("autoscaling")
    response = {}

    try:
        response = client.update_auto_scaling_group(
            AutoScalingGroupName = Params['AutoScalingGroupName'],
            LaunchConfigurationName = Params['LaunchConfigurationName']
        )
    except Exception as e:
        print(e)

    return response 

def GetInstanceId(InstanceName):
    client = GetClient()
    response = {}

    try:
        response = client.describe_instances(
            Filters = [
                {
                    'Name': 'tag:Name',
                    'Values': [ InstanceName, ],
                },
            ]
        )
    except Exception as e:
        pass
        #print(e)
    return response 

def DescribeLoadBalancer():
    client = GetClient("elbv2")
    response = None

    try:
        response = client.describe_load_balancers()
    except Exception as e:
        print(e)
    for i in response['LoadBalancers']:
        if i['LoadBalancerName'] == Instance['AlbName']:
            Instance.update({'LoadBalancerArn': i['LoadBalancerArn']})
            Instance.update({'LoadBalancerName': i['LoadBalancerName']})
            AsgInfo.update({'LoadBalancerNames': [ i['LoadBalancerName']]})
    try:        
        response = client.describe_target_groups(
            LoadBalancerArn = Instance['LoadBalancerArn']
        )
    except Exception as e:
        print(e)

    for i in response['TargetGroups']:
        AsgInfo.update({'TargetGroupARNs': [ i['TargetGroupArn']]})

if __name__ == '__main__':
    BeginTime = time.time()
    AmiId = ''
    response = {}
    NowTime = time.strftime("-%F-%H%M")
    AmiName = Instance['InstanceName'] + str(NowTime)

    Instance.update({'AmiName': AmiName})
    sgs = [] 
    response = GetInstanceId(Instance['InstanceName'])
    for i in response['Reservations']:
        for j in i['Instances']:
            Instance.update({'SubnetId': j['SubnetId']})
            Instance.update({'InstanceId': j['InstanceId']})
            for k in j['SecurityGroups']:
                sgs.append(k['GroupId'])
    
    #            Instance.update({'SecurityGroups': [ k['GroupId'], ]})
    #            LcInfo.update({'SecurityGroups': [ k['GroupId'], ]})
    Instance.update({'SecurityGroups': sgs })
    LcInfo.update({'SecurityGroups': sgs })
    DescribeLoadBalancer()

    Params = Instance
    try:
        response = CreateAmi(**Params)
        AmiId = response['ImageId']
        Instance.update({'ImageId': AmiId })
        LcInfo.update({'ImageId': AmiId})
    except Exception as e:
        print(e)
    time.sleep(5)

    Tags = CreateTags(AmiId , Instance['InstanceName'])
    # -- Create a Launch Configuration -- # 
    res = CreateLaunchConfiguration(**LcInfo)

    if CreateAsg == True:
        # -- Create A Auto Scaling Group -- # 
        response = CreateAutoScalingGroup(**AsgInfo)
    elif CreateAsg == False:
        # -- Update a auto Scaling Group , Like this -- # 
        Params['AutoScalingGroupName'] = AsgInfo['AutoScalingGroupName']
        Params['LaunchConfigurationName'] = LcInfo['LaunchConfigurationName']
        print(Params['LaunchConfigurationName'])
    else:
        pass

    print(" -- It took time  %s -- " % (time.time() - BeginTime))
