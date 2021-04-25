import numpy as np
import random
from typing import NamedTuple, List
from dataclasses import dataclass
import performance_metrics
import caching_algorithms
from caching_algorithms import is_online
import request_modals
import cost_modals
from src.utils import Results
from virtual_cache import VirtualCache
from simulation_instance import SimulationInstance
# import concurrent.futures
import multiprocessing


@dataclass
class Hyperparameters:
    ALGORITHMS: List[str]
    PERFORMANCE_METRIC: str
    NUM_OF_ITERATIONS: int
    NUM_OF_REQUESTS: int
    REQ_FREQUENCY: float  # Avg. number of requests arriving during a fetch
    ETA: float
    CACHE_SIZE: int
    MEMORY_SIZE: int
    LOG_FILE: str
    # QUITE: bool
    # HIT_WEIGHT: float
    # MISS_WEIGHT: float

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

# define types
# TODO add typeing
File = int
RequestSequence = [(float, File)]



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


    def batch_run(self):

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

    @staticmethod
    def run_simulations(algorithms, n_iter, n_requests, cache_size, library_size, performance_metric_name, request_frq, zipf_eta, seed):
        results = Results(algorithms, n_iter, n_requests, cache_size, library_size, performance_metric_name, request_frq, zipf_eta, seed)


        for algorithm in algorithms:

            # Initilise simulation parameters
            np.random.seed(seed)
            request_modal_gen = (request_modals.Zipfian(n_requests, library_size, eta=zipf_eta) for _ in range(n_iter))
            cost_modal_gen = (cost_modals.StaticUniformCost(library_size, request_frq) for _ in range(n_iter))

            total = 0
            for iteration in range(n_iter):
                log(f'begin')
                # initilise instance
                virtual_cache = VirtualCache(cache_size)
                print('#')
                request_modal = next(request_modal_gen)
                print('#')
                cost_modal = next(cost_modal_gen)
                print('#')
                caching_algorithm = caching_algorithms.get(algorithm, cache_size, cost_modal) if is_online(algorithm) else caching_algorithms.get(algorithm, cache_size, cost_modal, request_modal)
                print('#')
                performance_metric = performance_metrics.get(performance_metric_name, request_modal, virtual_cache.state(), cost_modal)
                print('#')
                sim = SimulationInstance(caching_algorithm, performance_metric, request_modal, cost_modal, virtual_cache)

                ## Simulate
                log(f'>>> Simulating {algorithm}...')
                sim_pm = sim.simulate()
                sim_pm.compute()
                total += sim_pm.result
                log(f'{algorithm} #{iteration+1} \t{sim_pm}\t', f'hit: {sim_pm.hit_count}  miss: {sim_pm.miss_count}')


            # log(f'>>> Simulating {algorithm}...')
            # p = multiprocessing.Pool(n_iter)
            # simulation_args = [(algorithm, next(request_sequence_gen), next(cost_func_gen)) for _ in range(n_iter)]
            # total = 0
            # for number, performance_result in enumerate(p.starmap(self.simulate, simulation_args)):
            #     total += performance_result.calculate()
            #     log(f'{algorithm} #{number+1} \t{performance_result}\t', f'hit: {performance_result.hit_count}  miss: {performance_result.miss_count}')


            results[algorithm] = total / n_iter

            log(f'>>> Average {performance_metric_name}: {results[algorithm]}\t(over {n_iter} simulations)\n')

        # log results as csv and formatted table
        log(f'{"-"*50} RAW DATA (CSV) \n'
            f'{results}\n'
            f'{"-"*50}\n\n'
            f'>>> RESULTS - (over {n_iter} simulations)\n'
            f'{results.table(sort=True)}\n\n')
            
        return results

    def create_instance(self, n_requests, cache_size, library_size, performance_metric_name, performance_metric_args, caching_algorithm_name, request_modal_name, request_modal_args, cost_modal_name, cost_modal_args, init_cache_state=None):
        virtual_cache = VirtualCache(cache_size, init_cache_state)
        request_modal = request_modals.get(request_modal_name, *request_modal_args)
        cost_modal = cost_modals.get(cost_modal_name, *cost_modal_args)

        if caching_algorithms.is_online(caching_algorithm_name):
            caching_algorithm = caching_algorithms.get(caching_algorithm_name, cache_size, cost_modal)
        else:
            caching_algorithm = caching_algorithms.get(caching_algorithm_name, cache_size, cost_modal, request_modal)
        performance_metric = performance_metrics.get(performance_metric_name, *performance_metric_args)

        return SimulationInstance(caching_algorithm, performance_metric, request_modal, cost_modal, virtual_cache)


def log(*param):
    print(*param)