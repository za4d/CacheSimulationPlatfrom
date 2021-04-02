from src.caching_algorithms import *


class CachingAlgorithm(object):
    def __init__(self, *params):
        self.params = params

    def get(self, name):
        if name == 'RR':
            return RandomReplacement(self.params.cost_function)
        elif name == 'FIFO':
            return FirstInFirstOut(*self.params)
        elif name == 'FILO':
            return FirstInLastOut(*self.params)
        elif name == 'LRU':
            return LeastRecentlyUsed(*self.params)
        elif name == 'LFU':
            return LeastFrequentlyUsed(*self.params)
        elif name == 'MIN':
            return Beladays(*self.params)
        elif name == 'MAD':
            return MinimumAggregateDelay(*self.params)
        # elif name == 'MAD-P':
        # 	return MinimumAggregateDelay_Perturbed(*self.params)
        elif name == 'MINAD':
            return MinimumAggregateDelay_Beladys(*self.params)
        elif name == 'MINAD-P':
            return MinimumAggregateDelay_Perturbed(*self.params)
        elif name == 'MINAD-L':
            return MinimumAggregateDelay_L(*self.params)
