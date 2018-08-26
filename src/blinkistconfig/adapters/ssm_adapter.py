import os
import boto3

REGION = os.environ['AWS_DEFAULT_REGION'] if 'AWS_DEFAULT_REGION' in os.environ else 'us-east-1'

DEFAULT_CLIENT = boto3.client('ssm', region_name=REGION)

class SSMAdapter():
    def get(self, key, scope=None, app_name=None, client=DEFAULT_CLIENT):
        prefix = "/application"
        key_scope = scope if scope else app_name
        return client.get_parameter(Name=f"{prefix}/{key_scope}/{key}", WithDecryption=True)
