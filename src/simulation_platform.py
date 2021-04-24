import numpy as np
import random
from typing import NamedTuple, List
from dataclasses import dataclass
import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
from virtual_cache import VirtualCache
# import concurrent.futures
import multiprocessing


@dataclass
class Hyperparameters:
    ALGORITHMS: List[str]
    PERFORMANCE_METRIC: str
    NUM_OF_ITERATIONS: int
    NUM_OF_REQUESTS: int
    Z: float  # Avg. number of requests arriving during a fetch
    ETA: float
    CACHE_SIZE: int
    MEMORY_SIZE: int
    LOG_FILE: str
    QUITE: bool
    HIT_WEIGHT: float
    MISS_WEIGHT: float

@dataclass
class Parameters:
    algorithm_name: str
    performance_metric: str
    caching_algorithm: str
    request_modal: str
    cost_modal: str
    num_of_iterations: int
    num_of_requests: int
    Z: float  # avg. number of requests arriving during a fetch
    eta: float
    cache_size: int
    memory_size: int
    log_file: str
    quite: bool
    hit_weight: float
    miss_weight: float



'''
# Simulation
- manages the simulation instances, generates the sequences of requests that will be simulated and the initial states 
of the simulations. Handles the simulations of the different algorithms. 
Number of repetitions
Algorithms to test
'''

class SimulationPlatform:
    def __init__(self, args):
        self.simulation_parameters = args[:-2]


    def run(self):

        for params in self.get_instances():
            performance_metric_args = None # TODO
            performance_metric = performance_metrics.get(name=params.performance_metric, args=performance_metric_args)
            caching_algorithm_args = None # TODO
            caching_algorithm = caching_algorithms.get(name=params.caching_algorithm, args=caching_algorithm_args)
            request_modal_args = None # TODO
            request_modal = request_modals.get(name=params.request_modal, args=request_modal_args)
            cost_modal_args = None # TODO
            cost_modal = cost_modals.get(name=params.cost_modal, args=cost_modal_args)
            init_state = list(np.random.randint(params.memory_size, size=params.cache_size))
            virtual_cache = VirtualCache(init_state)



        return results

    def get_instances(self):
        for sp in self.simulation_parameters:
            yield Parameters(*sp)

    def get_performance_metric(self, performance_metric_name: str, *params):
        if performance_metric_name == 'hit-ratio':
            return pm.HitRatio(*params)
        elif performance_metric_name == 'gain':
            return pm.Gain(*params)
        elif performance_metric_name == 'loss':
            return pm.LatencyLoss(*params)
        elif performance_metric_name == 'simpleloss':
            return pm.SimpleLoss(*params)

    def get_cost_function(self, mean, std):
        '''Returns a normally distributed dictionary of file costs'''
        # TODO: replace generators
        # TODO: change costs from a fixed mean to normal distribution
        while True:
            yield {file: mean for file in range(self.args.MEMORY_SIZE)}
            # yield {file: abs(np.random.normal(mean, std)) for file in range(self.args.MEMORY_SIZE)}


    def set_metric(self, metric_arg: str, *params):
        if metric_arg == 'hit-ratio':
            return pm.HitRatio(*params)
        elif metric_arg == 'gain':
            return pm.Gain(*params)
        elif metric_arg == 'loss':
            return pm.LatencyLoss(*params)
        elif metric_arg == 'simpleloss':
            return pm.SimpleLoss(*params)


    def log_results(self, results):
        args=self.args
        # log results as csv

        log('ALGORITHM,METRIC,RESULT,Z,ETA,N_ITER,N_REQUESTS,CACHE_SIZE,MEMORY_SIZE,SEED')
        for algorithm, result in results.items():
            log(f'{algorithm},{args.PERFORMANCE_METRIC},{result},{args.Z},{args.ETA},{args.NUM_OF_ITERATIONS},{args.NUM_OF_REQUESTS},{args.CACHE_SIZE},{args.MEMORY_SIZE},{args.SEED}')


