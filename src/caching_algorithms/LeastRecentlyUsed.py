
from src.caching_algorithms._caching_algorithms import CachingAlgorithm

class LeastRecentlyUsed(CachingAlgorithm):

    def __init__(self, cache_size):
        self.data = list(range(cache_size))

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            address = cache_state.index(requested_file)
            try:
                self.data.remove(address)
            except ValueError:
                pass
            self.data.append(address)
            return None
        else:
            replacement_address = self.data.pop(0)
            self.data.append(replacement_address)
            return replacement_address

    def online(self):
        return False

    def coded(self):
        return False



