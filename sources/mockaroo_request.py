from configparser import ConfigParser

class MockarooRequest:
    def __init__(self) -> None:
        self.key = None
        self.count = 0

    def to_string(self):
        return f'key:{self.key}, count:{self.count}'   