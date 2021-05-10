import numpy as np
# from _caching_algorithms import CachingAlgorithm
from caching_algorithms import OnlineCachingAlgorithm
from collections import deque


class FirstInFirstOut(OnlineCachingAlgorithm):
    name='FIFO'

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.cache_size = cache_size
        # list(range(len(self.storage)))
        self.stack = deque(range(cache_size))

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            return None
        else:
            replacement_address = self.stack.pop()
            self.stack.appendleft(replacement_address)
            return replacement_address

    # @property
    # def online(self):
    #     return False
    #
    # @property
    # def coded(self):
    #     return False

    @property
    def params(self):
        return None

