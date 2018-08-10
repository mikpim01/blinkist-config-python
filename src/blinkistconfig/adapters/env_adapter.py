import os

class EnvAdapter():
    def __init__(self):
        pass

    def get(self, key, scope=None):
        try:
            return os.environ[key]
        except:
            return None
