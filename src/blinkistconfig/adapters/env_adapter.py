import os

class ENVAdapter():
    def get(self, key, scope=None, app_name=None, client=None):
        key = key.replace("/", "_").upper()
        try:
            return os.environ[key]
        except:
            return None
