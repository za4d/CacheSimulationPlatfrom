from unittest import TestCase
import numpy as np
from tabulate import tabulate

import performance_metrics
import caching_algorithms
import request_modals
import library_modals
from simulation_instance import SimulationInstance
from recorder import Recorder
from simulation_platform import SimulationPlatform
from virtual_cache import VirtualCache
from caching_algorithms import caching_algorithms_all, caching_algorithms_online, caching_algorithms_offline


def test():
    # Example of a quick run
    s = SimulationPlatform().run_simulations(['RR', 'FIFO', 'LRU', 'LFU', 'LFU_IDEAL', 'MAD','MIN','MINAD'],
                                             n_iter=1,
                                             n_requests=999,
                                             cache_size=10,
                                             library_size=1000,
                                             performance_metric_names=['hit_ratio','latency_loss','simple_loss'],
                                             request_frq=1000,
                                             zipf_eta=1.5,
                                             seed = None)


def test_online_algorithms():
    performance_metric_names = ['hit_ratio','latency_loss','simple_loss']
    for algorithm in caching_algorithms_online:
        print('\t')
        # define instance parameters
        cache_size = 10
        library_size = 1000
        n_requests = 10000

        # set cache with its initial state
        virtual_cache = VirtualCache(np.random.choice(np.arange(0,library_size), size=cache_size, replace=False))

        # Create instances fro the request modals, library modals, caching algorithms adn perfromance metrc being simulated

        request_modal = request_modals.Zipfian(num_requests=n_requests, library_size=library_size, eta=1.7)

        library_modal = library_modals.StaticNormalCost(library_size, 100, 10)

        # Example of using get instead of a direct declaration (Note no request modal for online)
        caching_algorithm = caching_algorithms.get(algorithm, cache_size, library_modal) if caching_algorithms.is_online(algorithm) else caching_algorithms.get(algorithm, cache_size, library_modal, request_modal)

        # Create the instance recorder for the performance metrics to use
        recorder = Recorder()
        recorder.start(request_modal, virtual_cache.state(), library_modal)

        # Create and run the instance
        sim = SimulationInstance(caching_algorithm, recorder, request_modal, library_modal, virtual_cache)


        ## Simulate
        record = sim.simulate()
        for p,pm in zip(performance_metric_names,record.get_performances(performance_metric_names)):
            print(f'{algorithm}\t {p} : {pm.result}')

        # Post processing for the final result from the performance metric
    print('Done')



def test_offline_algorithms():
    performance_metric_names = ['hit_ratio','latency_loss','simple_loss']
    for algorithm in caching_algorithms_offline:
        print('\t')
        # define instance parameters
        cache_size = 10
        library_size = 1000
        n_requests = 10000

        # set cache with its initial state
        virtual_cache = VirtualCache(np.random.choice(np.arange(0,library_size), size=cache_size, replace=False))

        # Create instances fro the request modals, library modals, caching algorithms adn perfromance metrc being simulated

        request_modal = request_modals.Zipfian(num_requests=n_requests, library_size=library_size, eta=1.7)

        library_modal = library_modals.StaticNormalCost(library_size, 100, 10)

        # Example of using get instead of a direct declaration (Note no request modal for online)
        caching_algorithm = caching_algorithms.get(algorithm, cache_size, library_modal) if caching_algorithms.is_online(algorithm) else caching_algorithms.get(algorithm, cache_size, library_modal, request_modal)

        recorder = Recorder()
        recorder.start(request_modal, virtual_cache.state(), library_modal)


        # Create and run the instance
        sim = SimulationInstance(caching_algorithm, recorder, request_modal, library_modal, virtual_cache)

        ## Simulate
        record = sim.simulate()
        for p,pm in zip(performance_metric_names,record.get_performances(performance_metric_names)):
            print(f'{algorithm}\t {p} : {pm.result}')

        # Post processing for the final result from the performance metric
    print('Done')

def test_basic():
    SimulationPlatform().run_simulations(['RR','LFU','LRU','FIFO',], 3, 10000, 10, 1000, 'hit_ratio', 1000, 1.5, None)

def test_all():
    a = caching_algorithms_all
    SimulationPlatform().run_simulations(a, 10,  100000, 10, 1000, ['latency_loss','simple_loss','hit_ratio'], 1000, 1.5, None)




def test_multiple():
    # i,r = 10, 10000
    i,r = 3, 1000
    tabs = dict()
    zs = [np.power(10,p) for p in [0.00001,1,2, 2.33333333, 2.66666667, 3, 3.33333333,3.66666667, 4.,5,6]]
    for z in zs:
        r, s = SimulationPlatform().run_simulations(caching_algorithms_all, i,  r, 100, 1000, ['hit_ratio', 'latency_loss', 'simple_loss'], 1000, z, None)
        tabs[z] = s

    print('#'*100+'\n')

    for c,t in tabs.items(): print(f'# {c}\n',t)

if __name__ == '__main__':
    test_multiple()
    # test()
    # test_online_algorithms()
    # test_offline_algorithms()