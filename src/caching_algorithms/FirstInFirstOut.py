import numpy as np
# from _caching_algorithms import CachingAlgorithm
from src.caching_algorithms._caching_algorithms import CachingAlgorithm
from collections import deque


class FirstInFirstOut(CachingAlgorithm):

    def __init__(self, cache_size):
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

    def online(self):
        return False

    def coded(self):
        return False

# class FirstInFirstOut(CachingAlgorithm):
#
#     def __init__(self, cache_size):
#         super().__init__()
#         self.cache_size = cache_size
#         # self.data = list(range(cache_size))
#         self.queue = list(np.zeros(cache_size))
#
#     def __call__(self, file_request, time, cache_state):
#         if file_request in cache_state:
#             return None
#         else:
#             replacement_address = self.queue.pop(0)
#             self.queue.append(replacement_address)
#             return replacement_address