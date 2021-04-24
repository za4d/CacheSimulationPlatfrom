from dataclasses import dataclass
import numpy as np

from src.caching_algorithms._caching_algorithms import OnlineCachingAlgorithm

@dataclass
class FileMetadata:
    num_windows: int = 0
    cum_delay: float = 0
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

class MinimumAggregateDelay(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.track = TrackAggregateDelay(cost_modal)

    def __call__(self, time, requested_file, cache_state):
        self.track.tick()
        self.track.on_access(requested_file)
        if requested_file in cache_state:
            return  None
        else:
            replacement_address = np.argmin(map(self.track.estimate_aggregate_delay, cache_state))
            return replacement_address

