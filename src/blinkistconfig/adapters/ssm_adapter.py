import os
import boto3

DEFAULT_CLIENT = ""

class SSMAdapter():
    def get(self, key, scope=None, app_name=None, client=DEFAULT_CLIENT):
        key = key.replace("/", "_").upper()
        try:
            return os.environ[key]
        except:
            return None
