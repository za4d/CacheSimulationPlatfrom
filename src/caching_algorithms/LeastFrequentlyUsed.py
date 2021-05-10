
from caching_algorithms import OnlineCachingAlgorithm

class LeastFrequentlyUsed(OnlineCachingAlgorithm):
    name='LFU'

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
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

    # @property
    # def online(self):
    #     return True
    #
    # @property
    # def coded(self):
    #     return False
#
    @property
    def params(self):
        return None