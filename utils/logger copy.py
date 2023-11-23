# TODO: logger function

class _Logger():
    def __init__(self) -> None:
        pass


class SingletonLogger():

    # this should be the only actual logger existing
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = _Logger()
        return cls._instance

    def reset(self):
        self._instance = None


logger = SingletonLogger()
