import numpy as np
from caching_algorithms import OnlineCachingAlgorithm


# TODO: caching algorithms module

class RandomReplacement(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.cache_size = cache_size

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            return None
        else:
            return np.random.randint(self.cache_size)

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