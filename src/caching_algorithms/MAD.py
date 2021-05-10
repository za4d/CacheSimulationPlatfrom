from dataclasses import dataclass
import numpy as np

from caching_algorithms import OnlineCachingAlgorithm

@dataclass
class FileMetadata:
    num_windows: int = 0
    cum_delay: np.float64 = 0
    window_start: float = -np.inf

class TrackAggregateDelay:

    def __init__(self, cost_modal):
        self.time = 0
        self.metadata = dict()
        self.cost_func = cost_modal.cost

    def get_metadata(self, file):
        return self.metadata.setdefault(file, FileMetadata())

    def estimate_aggregate_delay(self, file):
        f = self.get_metadata(file)
        if f.num_windows == 0: return f.cum_delay * 0.1
        return np.float64(f.cum_delay) / f.num_windows

    def tick(self):
        self.time += 1

    def on_access(self, file):
        f = self.get_metadata(file)
        # time since start of previous miss mindow
        diff = self.time - f.window_start

        cost = self.cost_func(file)
        if diff >= cost:
            # start new window
            f.num_windows += 1
            f.cum_delay += cost
            f.window_start = self.time
        else:
            # accessed inside previous window
            f.cum_delay += cost - diff


# TODO
class MAD(OnlineCachingAlgorithm):
    name='MAD'

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.track = TrackAggregateDelay(cost_modal)

    def __call__(self, time, requested_file, cache_state):
        self.track.tick()
        self.track.on_access(requested_file)
        if requested_file in cache_state:
            return None
        else:
            replacement_address = np.argmin(list(map(self.track.estimate_aggregate_delay, cache_state)))
            return replacement_address

    @property
    def params(self):
        return None


# TODO
# class MAD(OnlineCachingAlgorithm):
#
#     def __init__(self, cache_size, cost_modal):
#         super().__init__(cache_size, cost_modal)
#         self.track = TrackAggregateDelay(cost_modal)
#
#     def __call__(self, time, requested_file, cache_state):
#         self.estimates(time, requested_file, cache_state)
#         replacement_address = np.argmin(self.estimates(time, requested_file, cache_state))
#         return replacement_address
#
#     def estimates(self, time, requested_file, cache_state):
#         self.track.tick()
#         self.track.on_access(requested_file)
#         if requested_file in cache_state:
#             return None
#         else:
#              return list(map(self.track.estimate_aggregate_delay, cache_state))
#
#     @property
#     def params(self):
#         return None
