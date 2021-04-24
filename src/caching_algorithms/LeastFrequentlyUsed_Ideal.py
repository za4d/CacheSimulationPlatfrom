import numpy as np

from src.caching_algorithms._caching_algorithms import OnlineCachingAlgorithm


class LeastFrequentlyUsedIdeal(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.frequency = {} # frequency by file

    def __call__(self, time, requested_file, cache_state):
        self.frequency.setdefault(requested_file, 1)
        if requested_file in cache_state:
            self.frequency[requested_file] += 1
            return None
        else:
            least_used_address = cache_state.index(min(cache_state, key=self.frequency.get))
            self.frequency[least_used_address] = 1
            return least_used_address

    # @property
    # def online(self):
    #     return True
    #
    # @property
    # def coded(self):
    #     return False
#
