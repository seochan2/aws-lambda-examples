import json
from botocore.vendored import requests
import boto3
import datetime

client = boto3.client('ce', 'us-east-1')

def mtd_cost(start, end):
    response = client.get_cost_and_usage(TimePeriod={'Start':start, 'End':end}, Granularity='MONTHLY', Metrics=['UnblendedCost'])
    amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    amount = round(float(amount), 2) 
    return amount

def lambda_handler(event, context):
    
    now = datetime.datetime.utcnow()
    start = now.strftime('%Y-%m-01')
    end = now.strftime('%Y-%m-%d')

    today_mtd_cost = mtd_cost(start, end)

    end = now - datetime.timedelta(days=1)
    end = end.strftime('%Y-%m-%d')

    yesterday_mdt_cost = mtd_cost(start, end)
    today_cost = today_mtd_cost - yesterday_mdt_cost

    today_cost = round(float(today_cost), 2)    
    
    slack_url = ""
    
    payloads = {
        "text": ' '.join(["Billing Notification", ":", end]),
        "attachments": [{
            "color": "#FFBB00",
            "fields": [{
                "title": "Current month-to-date balance", 
                "value": ' '.join(["$", str(today_mtd_cost)]),
                "short": False
            },{
                "title": "Yesterday balance", 
                "value": ' '.join(["$", str(today_cost)]),
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
