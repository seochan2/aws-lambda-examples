import boto3

session = boto3.Session(
    region_name="ap-northeast-1"
)

sns_client = session.client('sns')

def lambda_handler(event, context):
    response = sns_client.publish(
        PhoneNumber='',
        Message=''
    )
    
    print(response)
    
    return 'OK'