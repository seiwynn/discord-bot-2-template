# TODO: logger function

class SimpleLogger():
    def __init__(self) -> None:
        pass

# this should be the only actual logger existing.
class SingletonLogger():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = SimpleLogger()
        return cls._instance