import json
from botocore.vendored import requests
import boto3
import datetime

client = boto3.client('ce', 'us-east-1')

def lambda_handler(event, context):
    
    now = datetime.datetime.utcnow()
    
    start = now - datetime.timedelta(days=2)
    end = now - datetime.timedelta(days=1)
    
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')

    response = client.get_cost_and_usage(TimePeriod={'Start': start, 'End': end}, Granularity='DAILY', Metrics=['BlendedCost'])
    blended_cost = response['ResultsByTime'][0]['Total']['BlendedCost']

    slack_url = ""

    payloads = {
        "text": "Billing Notification",
        "attachments": [{
            "color": "#FFBB00",
            "fields": [{
                "title": start, 
                "value": str(round(float(blended_cost['Amount']), 2)) + ' ' + str(blended_cost['Unit']),
                "short": False
            }]
        }]
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }
