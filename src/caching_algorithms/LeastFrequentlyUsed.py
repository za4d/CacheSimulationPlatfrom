
from src.caching_algorithms._caching_algorithms import CachingAlgorithm

class LeastFrequentlyUsed(CachingAlgorithm):

    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.frequency = {i: 0 for i in range(cache_size)} # frequency by cache address slots

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            address = cache_state.index(requested_file)
            self.frequency[address] += 1
            return None
        else:
            least_used_address = min(self.frequency, key=self.frequency.get)
            self.frequency[least_used_address] = 1
            return least_used_address

    def online(self):
        return False

    def coded(self):
        return False
#
