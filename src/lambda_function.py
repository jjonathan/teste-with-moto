import boto3

def lambda_handler(event):
    client = boto3.client('ssm', region_name='sa-east-1')
    parametro = client.get_parameter(Name=event)
    return parametro['Parameter']['Value']
