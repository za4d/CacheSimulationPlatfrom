import numpy as np

from caching_algorithms import OnlineCachingAlgorithm


class LeastFrequentlyUsedIdeal(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.frequency = dict.fromkeys(cost_modal.asdict().keys(), 0)# frequency by file

    def __call__(self, time, requested_file, cache_state):
        self.frequency.setdefault(requested_file, 0)
        self.frequency[requested_file] += 1
        if requested_file in cache_state:
            return None
        else:
            least_used_address = cache_state.index(min(cache_state, key=self.frequency.get))
            return least_used_address

    def update(self, time, requested_file, cache_state):
        self.frequency.setdefault(requested_file, 0)
        self.frequency[requested_file] += 1

    # @property
    # def online(self):
    #     return True

    # @property
    # def coded(self):
    #     return False

    @property
    def params(self):
        return None