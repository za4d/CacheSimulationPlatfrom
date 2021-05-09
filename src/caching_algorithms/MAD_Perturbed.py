from dataclasses import dataclass
import numpy as np

from caching_algorithms import OnlineCachingAlgorithm

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

class MAD_Perturbed(OnlineCachingAlgorithm):

    def __init__(self, cache_size, cost_modal):
        super().__init__(cache_size, cost_modal)
        self.track = TrackAggregateDelay(cost_modal)
        self.perturbation_scale = np.power(4 * np.pi * np.log(10000), -1/4) * np.sqrt(10000/cache_size)
        self.init_state = [np.random.randint(len(cost_modal)) for _ in range(cache_size)]


    def __call__(self, time, requested_file, cache_state):
        if time==1:
            cache_state =  self.init_state
        self.track.tick()
        self.track.on_access(requested_file)
        if requested_file in cache_state:
            return  None
        else:
            replacement_address = np.argmin(map(self.perturbed_estimate_aggregate_delay, cache_state))
            return replacement_address

    def perturbed_estimate_aggregate_delay(self, file):
        perturbation = np.random.normal(0, 100)
        return self.track.estimate_aggregate_delay(file) + self.perturbation_scale * perturbation


    @property
    def params(self):
        return None
