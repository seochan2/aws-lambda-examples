import json
from botocore.vendored import requests
import boto3
import datetime

client = boto3.client('ce', 'us-east-1')

def lambda_handler(event, context):
    
    now = datetime.datetime.utcnow()
    start = now.strftime('%Y-%m-01')
    end = now.strftime('%Y-%m-%d')

    response = client.get_cost_and_usage(TimePeriod={'Start':start, 'End':end}, Granularity='MONTHLY', Metrics=['UnblendedCost'])
    amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    today_mtd_cost = round(float(amount), 2) 

    slack_url = ""
    
    payloads = {
        "text": ' '.join(["Billing Notification", ":", end]),
        "attachments": [{
            "color": "#FFBB00",
            "fields": [{
                "title": "Current month-to-date balance", 
                "value": ' '.join(["$", str(today_mtd_cost)]),
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