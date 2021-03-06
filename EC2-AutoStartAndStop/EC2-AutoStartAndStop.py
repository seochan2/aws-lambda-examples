import boto3
import time
from datetime import datetime, timedelta 

region = 'ap-northeast-2'
# EC2 Instance ID in list format
targetEC2InstanceIds = ['','']
targetRDSInstanceIdentifier = ''

def lambda_handler(event, context):
    
    seoulDT = datetime.today() + timedelta(hours=9)
    weekStr = seoulDT.strftime("%a")
    
    if weekStr in ['Sat', 'Sun']:
        print("don't work on weekends")
        return 0
    
    ec2Resource = boto3.resource('ec2')
    targetInstanceState = ec2Resource.Instance(targetEC2InstanceIds[0]).state['Name']
    
    ec2Client = boto3.client('ec2', region_name=region)
    rdsClient = boto3.client('rds', region_name=region)
    
    if targetInstanceState == 'running':
        ec2Client.stop_instances(InstanceIds=targetEC2InstanceIds)
        time.sleep(60)
        rdsClient.stop_db_instance(DBInstanceIdentifier=targetRDSInstanceIdentifier)
        print "EC2 is Stopping..."
    else:
        rdsClient.start_db_instance(DBInstanceIdentifier=targetRDSInstanceIdentifier)
        time.sleep(180)
        ec2Client.start_instances(InstanceIds=targetEC2InstanceIds)
        print "EC2 is starting..."