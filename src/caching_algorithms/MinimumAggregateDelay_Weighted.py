from caching_algorithms import MinimumAggregateDelay
from math import ceil


class MinimumAggregateDelayWeighted(MinimumAggregateDelay):
    name='MINAD_W'

    def __init__(self, cache_size, cost_modal, request_sequence, scale=0.011):
        super().__init__(cache_size, cost_modal, request_sequence)
        self.request_sequence_data = self.request_sequence.aslist()
        self.scale = scale

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
            time_saved = dict()
            for address, file in enumerate(cache_state+[requested_file]):
                # get Time Until Next Request
                try:
                    tunr = self.request_sequence_data.index(file) + 1

                except ValueError:
                    # tunr = np.inf
                    # if file is never requested again remove it
                    return address

                # get Aggregate Delay
                agg_delay = self.aggregate_delay(file, tunr-1)

                time_saved[address] = agg_delay / (tunr ** self.scale)

            # replace file which saves the least amount of time
            replacement_address = min(time_saved, key=time_saved.get)

            if replacement_address>len(cache_state)-1:
                return -1

            return replacement_address

    @property
    def params(self):
        return None