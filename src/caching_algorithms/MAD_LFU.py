from dataclasses import dataclass
import numpy as np
from caching_algorithms import MAD, TrackAggregateDelay

from caching_algorithms import OnlineCachingAlgorithm, LeastFrequentlyUsedIdeal


class MAD_LFU(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.track = TrackAggregateDelay(cost_modal)
        self.lfu = LeastFrequentlyUsedIdeal(cache_size, cost_modal)

    def __call__(self, time, requested_file, cache_state):
        self.lfu.update(time,requested_file,cache_state)
        self.track.tick()
        self.track.on_access(requested_file)
        if requested_file in cache_state:
            return None
        else:
            # for cache_address, frequency:
            #     pass
            replacement_address = np.argmin(list(map(self.rank, cache_state)))
            return replacement_address

    def rank(self, file):
        ad = self.track.estimate_aggregate_delay(file)
        ad = 1
        tunr = 1 * self.lfu.frequency.get(file)
        return tunr

    @property
    def params(self):
        return None
