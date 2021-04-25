from collections import deque
from caching_algorithms import OnlineCachingAlgorithm


class FirstInLastOut(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        # list(range(len(self.storage)))
        self.stack = list(range(cache_size))

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            return None
        else:
            replacement_address = self.stack.pop()
            self.stack.append(replacement_address)
            return replacement_address

    # @property
    # def online(self):
    #     return True
    #
    # @property
    # def coded(self):
    #     return False
