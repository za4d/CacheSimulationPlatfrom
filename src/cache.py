import numpy as np


class Cache(list):

    def __init__(self, length, init_state=None):
        if init_state:
            super().__init__(init_state)
        else:
            super().__init__([0] * length)

    def store(self, file, replacement_address):
        self.__setitem__(replacement_address, file)

