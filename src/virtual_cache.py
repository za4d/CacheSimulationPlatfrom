
class VirtualCache(list):

    def __init__(self, cache_size=None, init_state=None):
        if init_state is not None:
            super().__init__(init_state)
        elif cache_size is not None:
            super().__init__([0]*cache_size)
        else:
            raise TypeError("VirtualCache takes at least 1 positional argument (0 given)")

    def read(self, address):
        return super().__getitem__(address)

    def write(self, address, file):
        super().__setitem__(address, file)

    def state(self):
        return self.copy()
