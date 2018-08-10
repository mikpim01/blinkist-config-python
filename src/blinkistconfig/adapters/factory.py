import blinkistconfig.adapters

class Factory:
    @staticmethod
    def by(type):
        return getattr(blinkistconfig.adapters, f"{type}Adapter")()
