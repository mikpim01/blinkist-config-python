import os
import boto3

DEFAULT_CLIENT = ""

class SSMAdapter():
    def __init__(self, client=DEFAULT_CLIENT):
        self.client = client

    def get(self, key, scope=None):
        key = key.replace("/", "_").upper()
        try:
            return os.environ[key]
        except:
            return None
