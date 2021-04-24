class :

    def __init__(self, cache_size):
        pass

    def __call__(self, time, requested_file, cache_state):
        if requested_file in cache_state:
            return None
        else:
            return

    def online(self):
        return False

    def coded(self):
        return False
# MinimumAggregateDelay_Perturbed
