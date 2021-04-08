

class SimulationInstance:


    # def __init__(self, algorithm_name, performance_metric, request_modal, library_modal, init_state: List[File]):
    #     self.storage = init_state
    #     self.caching_algorithm = self.set_algorithm(algorithm_name)
    #     cost_func = library_modal.costfunct()
    #     if algorithm_name in ['MAD', 'MAD-P', 'MINAD']:
    #         self.track = TrackAggregateDelay(cost_func)
    #     elif algorithm_name == 'MINAD-P':
    #         self.perturbation_scale = np.power(4 * np.pi * np.log(len(data)), -1/4) * np.sqrt(len(data)/len(init_state))


    def __init__(self, caching_algorithm, performance_metric, request_modal, communication_modal, init_state=None):
        self.caching_algorithm = caching_algorithm
        self.performance_metric = performance_metric
        self.request_modal = request_modal
        self.communication_modal = communication_modal
        self.cache_storage = init_state



    def simualte(self):
        # performace_metric = self.set_metric(self.args.PERFORMANCE_METRIC, cost_func, self.args.HIT_WEIGHT, self.args.MISS_WEIGHT)
        # # initialise cache with random files
        # cache_state = list(np.random.randint(self.args.MEMORY_SIZE, size=self.args.CACHE_SIZE))
        # cac
        # data = None
        #
        # if algorithm_name in ['MIN', 'MINAD', 'MINAD-P', 'MINAD-L']:
        #     data = request_sequence.copy()
        #
        # if init_state is not None:
        #     cache_state = init_state.copy()
        #
        # cache = Cache(cache_state, algorithm_name, data, cost_func)



        for file in self.request_modal:
            # caching algorithm takes requested file??? and returns file to be replaced file
            replacement_address = cache.caching_algorithm(file, self.performace_metric)
            if replacement_address is not None:
                cache.replace(replacement_address, file)

        return performace_metric

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
