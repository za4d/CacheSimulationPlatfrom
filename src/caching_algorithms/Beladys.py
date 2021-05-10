from caching_algorithms import OfflineCachingAlgorithm


# TODO: caching algorithms module

class Beladys(OfflineCachingAlgorithm):
    name='MIN'

    def __init__(self, cache_size, cost_modal, request_sequence):
        super().__init__(cache_size, cost_modal, request_sequence)
        self.request_sequence_data = self.request_sequence.aslist()

    def __call__(self, time, requested_file, cache_state):
        self.request_sequence_data.remove(requested_file)
        if requested_file in cache_state:
            return None
        else:

            # Don't cache if no requested again
            if requested_file not in self.request_sequence_data:
                return None

            # Find cached file with furthest next request
            replacement_address = furthest_request = 0
            for address, file in enumerate(cache_state):
                try:
                    tunr = self.request_sequence_data.index(file) + 1
                except ValueError:
                    replacement_address = address
                    break
                if tunr > furthest_request:
                    furthest_request = tunr
                    replacement_address = address

            return replacement_address

    @property
    def params(self):
        return None