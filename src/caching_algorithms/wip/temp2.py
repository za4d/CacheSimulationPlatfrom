from src.caching_algorithms._caching_algorithms import OfflineCachingAlgorithm

class (OfflineCachingAlgorithm):

    def __init__(self, cache_size):
        self.cache_size = cache_size

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:

        else:

# TEMP2
