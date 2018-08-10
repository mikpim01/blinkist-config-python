from blinkistconfig import adapters

class Config:
    """
    Config represents a single configuration store. The interface is kept minimal
    with a single method to get a specific key from the store.

    ## Example
        config = Config()
        config.env = "production"
    """
    env = ""
    adapter_type = ""

    @classmethod
    # The *args is passed that way to handle None default values properly
    def get(cls, key, *args, scope=None):
        """
        Returns the value of the key from the store or the default value if store
        fails
        """
        cls._validate_params(*args)
        adapter_value = cls._adapter()

        return key

    @staticmethod
    def _has_default(*args):
        return len(args) == 1

    @staticmethod
    def _default_value(*args):
        return args[0]

    @staticmethod
    def _validate_params(*args):
        args_length = len(args)
        error_message = f"wrong number of arguments"

        if args_length not in [0, 1]:
            raise ValueError(error_message)

    @classmethod
    def _adapter(cls):
        cls.adapter = getattr(cls, "adapter", adapters.Factory.by(cls.adapter_type))
        return cls.adapter
