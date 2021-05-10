
from caching_algorithms import OnlineCachingAlgorithm

class LeastRecentlyUsed(OnlineCachingAlgorithm):
    name='LRU'

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
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

