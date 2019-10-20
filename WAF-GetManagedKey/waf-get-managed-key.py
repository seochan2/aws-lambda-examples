import boto3

def lambda_handler(event, context):
    
    client = boto3.client('waf-regional')
    rules = client.list_rate_based_rules()
    
    for rule_info in rules['Rules']:
        print('RuleId : ', rule_info['RuleId'])
        print('Name : ', rule_info['Name'])
        
        response = client.get_rate_based_rule_managed_keys(RuleId=rule_info['RuleId'])
        
        managed_keys = response['ManagedKeys']
        print('IPs : ', managed_keys)
        
    return 'OK'


