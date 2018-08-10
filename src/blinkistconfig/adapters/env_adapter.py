import os

class EnvAdapter():
    def __init__(self):
        pass

    def get(self, key, scope=None):
        key = key.replace("/", "_").upper()
        try:
            return os.environ[key]
        except:
            return None
