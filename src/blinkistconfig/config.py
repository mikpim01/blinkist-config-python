from blinkistconfig import adapters
from blinkistconfig import errors

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
    app_name = ""

    @classmethod
    # The *args is passed that way to handle None default values properly
    def get(cls, key, *args, scope=None):
        """
        Returns the value of the key from the store or the default value if store
        fails
        """
        cls._validate_params(*args)
        from_adapter = cls._adapter().get(key, scope=scope)

        if from_adapter == None:
            cls._value_missing(key, *args, scope=scope)
        else:
            return from_adapter

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

    @staticmethod
    def _handle_error(key, scope):
        raise errors.ValueMissingError(f"key: {key} has no value in {scope}")

    @classmethod
    def _value_missing(cls, key, *args, scope):
        if cls._has_default(*args):
            return cls._default_value(*args)
        cls._handle_error(key, scope)
