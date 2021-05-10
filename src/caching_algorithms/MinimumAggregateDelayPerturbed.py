import numpy as np
from caching_algorithms import MinimumAggregateDelay
from math import ceil

class MinimumAggregateDelayPerturbed(MinimumAggregateDelay):

    def __init__(self, cache_size, cost_modal, request_sequence):
        super().__init__(cache_size, cost_modal, request_sequence)
        self.request_sequence_data = self.request_sequence.aslist()
        self.perturbation_scale = np.power(4 * np.pi * np.log(len(request_sequence)), -1/4) * np.sqrt(len(request_sequence)/cache_size)

    def __call__(self, time, requested_file, cache_state):
        self.request_sequence_data.remove(requested_file)
        if requested_file in cache_state:
            return None
        else:
            # Don't cache if file it will never be requested again
            if requested_file not in self.request_sequence_data:
                return None

            # Fin
            # Timed save per tick if file is kept in cache
            perturbed_time_saved = dict()
            for address, file in enumerate(cache_state):

                # Get perturbation
                perturbation = np.random.normal(0, 1)

                # Get Time Until Next Request
                try:
                    tunr = self.request_sequence_data.index(file) + 1
                except ValueError:
                    # tunr = np.inf
                    # if file is never requested again remove it
                    return address

                # Get Aggregate Delay
                agg_delay = self.aggregate_delay(file, tunr)

                perturbed_time_saved[address] = agg_delay / tunr + self.perturbation_scale * perturbation

            # replace file which saves the least amount of time
            replacement_address = min(perturbed_time_saved, key=perturbed_time_saved.get)

            return replacement_address


    @property
    def params(self):
        return None