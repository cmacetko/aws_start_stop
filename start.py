import boto3

region = 'us-east-1'
instances = ['ID_DA_INSTANCIA']

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)