import os

class ENVAdapter():
    def get(self, key, scope=None, app_name=None, client=None):
        key = key.replace("/", "_").upper()
        return os.environ.get(key)
