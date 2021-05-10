from dataclasses import dataclass
import numpy as np

from caching_algorithms import OnlineCachingAlgorithm
from caching_algorithms import MAD, TrackAggregateDelay



class MADPerturbed(OnlineCachingAlgorithm):

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
            replacement_address = np.argmin(list(map(self.perturbed_estimate_aggregate_delay, cache_state)))
            # replacement_address = np.argmin(map(self.perturbed_estimate_aggregate_delay, cache_state))
            return replacement_address

    def perturbed_estimate_aggregate_delay(self, file):
        perturbation = np.random.normal(0, 100)
        return self.track.estimate_aggregate_delay(file) + self.perturbation_scale * perturbation


    @property
    def params(self):
        return None
