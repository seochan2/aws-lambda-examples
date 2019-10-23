import json
import boto3
import datetime

client = boto3.client('ce', 'us-east-1')

def lambda_handler(event, context)

    now = datetime.datetime.utcnow()
    
    start = now - datetime.timedelta(days=2)
    end = now - datetime.timedelta(days=1)
    
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')
    
    response = client.get_cost_and_usage(TimePeriod={'Start': start, 'End': end}, Granularity='DAILY', Metrics=['BlendedCost'])
    blended_cost = response['ResultByTime'][0]['Total']['BlendedCost']
    
    amount = blended_cost['Amount']
    unit = blended_cost['Unit']
    
    result = str(round(float(amount), 2)) + ' ' + str(unit)
    
    return {
        'statusCode': 200,
        'body': json.dumps(['result', {'date': start}, {'cost': result}])
    }