from caching_algorithms import OfflineCachingAlgorithm, MinimumAggregateDelay
from math import ceil

class MinimumAggregateDelayLayered(MinimumAggregateDelay):
    name='MINAD_L'

    def __init__(self, cache_size, cost_modal, request_sequence):
        super().__init__(cache_size, cost_modal, request_sequence)
        self.request_sequence_data = self.request_sequence.aslist()

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
            metadata = dict()
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

                metadata[address] = (agg_delay, tunr)

            # replace file which saves the least amount of time
            min_agg = min([agg for agg, _ in metadata.values()])
            # min_agg_addresses = {address: tunr for address, (agg_delay, tunr) in metadata.items() if agg_delay == min_agg}
            # out of the smallest aggdelays select the on with the largest time until nex request
            min_agg_addresses = {address: tunr for address, (agg_delay, tunr) in metadata.items() if agg_delay == min_agg}
            # if len(min_agg_addresses) > 1:
            #     print('!')
            replacement_address = max(min_agg_addresses, key=min_agg_addresses.get)

            if replacement_address>len(cache_state)-1:
                return -1

            return replacement_address


    @property
    def params(self):
        return None