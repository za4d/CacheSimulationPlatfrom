from collections import deque
from src.caching_algorithms._caching_algorithms import CachingAlgorithm


class FirstInLastOut(CachingAlgorithm):

    def __init__(self, cache_size):
        self.cache_size = cache_size
        # list(range(len(self.storage)))
        self.stack = list(range(cache_size))

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            return None
        else:
            replacement_address = self.stack.pop()
            self.stack.append(replacement_address)
            return replacement_address

    def online(self):
        return False

    def coded(self):
        return False
