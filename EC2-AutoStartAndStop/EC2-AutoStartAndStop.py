import boto3
region = 'ap-northeast-2'
# EC2 Instance ID in list format
targetEC2InstanceIds = ['','']
targetRDSInstanceIdentifier = ''

def lambda_handler(event, context):
    
    ec2Resource = boto3.resource('ec2')
    targetInstanceState = ec2Resource.Instance(targetEC2InstanceIds[0]).state['Name']
    
    ec2Client = boto3.client('ec2', region_name=region)
    rdsClient = boto3.client('rds', region_name=region)
    
    if targetInstanceState == 'running':
        ec2Client.stop_instances(InstanceIds=targetEC2InstanceIds)
        rdsClient.stop_db_instance(DBInstanceIdentifier=targetRDSInstanceIdentifier)
        print "EC2 is Stopping..."
    else:
        ec2Client.start_instances(InstanceIds=targetEC2InstanceIds)
        rdsClient.stop_db_instance(DBInstanceIdentifier=targetRDSInstanceIdentifier)
        print "EC2 is starting..."