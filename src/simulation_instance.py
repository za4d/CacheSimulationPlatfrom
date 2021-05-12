import numpy as np


class SimulationInstance:

    # def __init__(self, algorithm_name, performance_metric, request_modal, library_modal, init_state: List[File]):
    #     self.storage = init_state
    #     self.caching_algorithm = self.set_algorithm(algorithm_name)
    #     cost_func = library_modal.costfunct()
    #     if algorithm_name in ['MAD', 'MAD-P', 'MINAD']:
    #         self.track = TrackAggregateDelay(cost_func)
    #     elif algorithm_name == 'MINAD-P':
    #         self.perturbation_scale = np.power(4 * np.pi * np.log(len(data)), -1/4) * np.sqrt(len(data)/len(init_state))

    def __init__(self, caching_algorithm, recorder, request_modal, cost_modal, virtual_cache):
        self.cache = virtual_cache
        self.caching_algorithm = caching_algorithm
        self.performance_metric = recorder
        self.request_modal = request_modal
        self.cost_modal = cost_modal

    def simulate(self):
        cache = self.cache
        caching_algorithm = self.caching_algorithm
        performance_metric = self.performance_metric
        request_modal = self.request_modal

        for time, file in request_modal:
            # caching algorithm takes requested file??? and returns file to be replaced file
            replacement_address = caching_algorithm(time, file, cache)
            # print(replacement_address)
            if replacement_address is not None:
                cache.write(replacement_address, file)
            performance_metric.record(time, replacement_address)

        return performance_metric

    # def set_algorithm(self, name):
    #     if name == 'RR':
    #         return RandomReplacement(self.params.cost_function)
    #     elif name == 'FIFO':
    #         return FirstInFirstOut(*self.params)
    #     elif name == 'FILO':
    #         return FirstInLastOut(*self.params)
    #     elif name == 'LRU':
    #         return LeastRecentlyUsed(*self.params)
    #     elif name == 'LFU':
    #         return LeastFrequentlyUsed(*self.params)
    #     elif name == 'MIN':
    #         return Beladays(*self.params)
    #     elif name == 'MAD':
    #         return MinimumAggregateDelay(*self.params)
    #     # elif name == 'MAD-P':
    #     # 	return MinimumAggregateDelay_Perturbed(*self.params)
    #     elif name == 'MINAD':
    #         return MinimumAggregateDelay_Beladys(*self.params)
    #     elif name == 'MINAD-P':
    #         return MinimumAggregateDelay_Perturbed(*self.params)
    #     elif name == 'MINAD-L':
    #         return MinimumAggregateDelay_L(*self.params)
