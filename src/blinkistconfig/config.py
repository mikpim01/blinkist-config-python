class Config:
    env = ""

    @classmethod
    # The *args is passed that way to handle None default values properly
    def get(cls, key, *args, scope=None):
        """
        Returns the value of the key from the store or the default value if store
        fail
        """
        cls.validate_default(*args)

        return key

    @staticmethod
    def _has_default(*args):
        return len(args) == 1

    @staticmethod
    def _default_value(*args):
        return args[0]

    @staticmethod
    def validate_default(*args):
        args_length = len(args)
        error_message = f"wrong number of arguments"

        if args_length not in [0, 1]:
            raise ValueError(error_message)
