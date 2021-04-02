import numpy as np
import random
from typing import NamedTuple, List
from dataclasses import dataclass
from src.performance_metrics import PerformanceMetric
from src.caching_algorithms import CachingAlgorithm
from src.request_modals import RequestModal
from src.communication_modals import LibraryModal
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
    SEED: int

@dataclass
class Parameters:
    algorithm_name: str
    performance_metric: str
    caching_algorithm: str
    request_modal: str
    file_library: str
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
    seed: int



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


    def run_simulations(self):

        for params in self.get_instances():
            performance_metric_args = None # TODO
            performance_metric = PerformanceMetric(params).get(name=params.performance_metric)
            caching_algorithm_args = None # TODO
            caching_algorithm = CachingAlgorithm(params).get(name=params.caching_algorithm)
            request_modal_args = None # TODO
            request_modal = RequestModal(params).get(name=params.request_modal)
            file_library_args = None # TODO
            file_library = LibraryModal(params).get(name=params.file_library)





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
        np.random.seed(self.seed)
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


