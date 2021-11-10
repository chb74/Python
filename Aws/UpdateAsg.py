# -- By liverpools@gmail.com -- # 
# -- On Mar 6, 2018 -- # 
import boto3, time 

# -- This is a Session for AWS Connection -- # 
def GetClient(Service):
    session = boto3.Session()
    client = session.client(Service)

    return client

# -- Updates some Auto Scaling Group -- # 
def UpdateAutoScalingGroup(**Params):
    client = GetClient("autoscaling")
    response = None 

    try:
        response = client.update_auto_scaling_group(
            AutoScalingGroupName = Params['Name'],
            MinSize = Params['Min'],
            MaxSize = Params['Max'],
            DesiredCapacity = Params['Desire'],
        )
    except Exception as e:
        print(e)
    print(response)

# -- def lambda_handler(event, context):
if __name__=="__main__":
    BeginTime = time.time() 
    Params = [
       { 'Name' : 'Prd-Asg', 'Max': 8, 'Min': 4, 'Desire': 4 },
       { 'Name' : 'Stg-Asg', 'Max': 8, 'Min': 4, 'Desire': 4 },
       { 'Name' : 'Dev-Asg', 'Max': 8, 'Min': 4, 'Desire': 4 },

    ]

    for i in Params:
        UpdateAutoScalingGroup(**i)
    print("It took time %s sec", (time.time() - BeginTime)) 
