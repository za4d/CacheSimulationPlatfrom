from dataclasses import dataclass
import numpy as np
from caching_algorithms import TrackAggregateDelay, OnlineCachingAlgorithm

from caching_algorithms import OfflineCachingAlgorithm, LeastFrequentlyUsedIdeal


# class MAD_LFU(OnlineCachingAlgorithm):
#
#     def __init__(self, cache_size, cost_modal):
#         super().__init__(cache_size, cost_modal)
#         self.track = TrackAggregateDelay(cost_modal)
#         self.lfu = LeastFrequentlyUsedIdeal(cache_size, cost_modal)
#
#     def __call__(self, time, requested_file, cache_state):
#         self.lfu.update(time,requested_file,cache_state)
#         self.track.tick()
#         self.track.on_access(requested_file)
#         if requested_file in cache_state:
#             return None
#         else:
#             # for cache_address, frequency:
#             #     pass
#             replacement_address = np.argmin(list(map(self.rank, cache_state)))
#             return replacement_address
#
#     def rank(self, file):
#         ad = self.track.estimate_aggregate_delay(file)
#         ad = 1
#         tunr = 100 * (self.lfu.frequency.get(file) +1)
#         return ad/tunr
#
#     @property
#     def params(self):
#         return None



class MAD_MIN(OfflineCachingAlgorithm):
    name='MAD_MIN'

    def __init__(self, cache_size, cost_modal, request_sequence):
        super().__init__(cache_size, cost_modal, request_sequence)
        self.track = TrackAggregateDelay(cost_modal)
        self.request_sequence_data = self.request_sequence.aslist()

    def __call__(self, time, requested_file, cache_state):
        # self.lfu.update(time,requested_file,cache_state)
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
        tunr = self.beladys_tunr(file)
        return ad / tunr
        # return ad/tunr if tunr>0 else ad*0.001

    def beladys_tunr(self, requested_file):
        try:
            tunr = self.request_sequence_data.index(requested_file) + 1
        except ValueError:
            tunr = np.inf

        return tunr
    @property
    def params(self):
        return None

class MAD_LFU2(OnlineCachingAlgorithm):
    name='MAD_LFU2'

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
            replacement_address = np.argmin(list(map(self.rank, cache_state+[requested_file])))
            if replacement_address>len(cache_state)-1:
                return None
            return replacement_address

    def rank(self, file):
        ad = self.track.estimate_aggregate_delay(file)
        tunr = self.lfu.frequency.get(file)
        return ad * tunr
        # return ad/tunr if tunr>0 else ad*0.001

    @property
    def params(self):
        return None

