from unittest import TestCase
import numpy as np
from tabulate import tabulate

import performance_metrics
import caching_algorithms
import request_modals
import library_modals
import simulation_instance
from simulation_platform import SimulationPlatform
from virtual_cache import VirtualCache
from caching_algorithms import caching_algorithms_all, caching_algorithms_online, caching_algorithms_offline
# class TestAlgorithms(TestCase):
#
#     def t(self):
#         print('Y')

def test_online_algorithms():
    for caching_algorithm_name in ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MAD']:
        c = 10
        n = 1000
        r = 10000
        vc = VirtualCache(c)
        rm = request_modals.Zipfian(num_requests=r, library_size=n, eta=1.7)
        cm = library_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
        ###
        ca = caching_algorithms.get(caching_algorithm_name, c, cm)
        ###
        pm = performance_metrics.HitRatio(rm, vc, cm)
        sim = simulation_instance.SimulationInstance(ca, pm, rm, cm, vc)
        metric = sim.simulate()
        metric.compute()
        print(caching_algorithm_name, metric)
    print('Done')
        # return str(metric)



def test_offline_algorithms():

    for caching_algorithm_name in ['MIN', 'MINAD', 'MINAD-P', 'MINAD-L']:
        cache_size = 10
        library_size = 1000
        n_requests = 10000
        virtual_cache = VirtualCache(cache_size)
        request_modal = request_modals.Zipfian(num_requests=n_requests, library_size=library_size, eta=1.7)
        # cost_modal = library_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
        cost_modal = library_modals.StaticNormalCost(library_size, 100, 10)
        ###
        caching_algorithm = caching_algorithms.get(caching_algorithm_name, cache_size, cost_modal, request_modal)
        ###
        performance_metric = performance_metrics.HitRatio(request_modal, virtual_cache, cost_modal)
        sim = simulation_instance.SimulationInstance(caching_algorithm, performance_metric, request_modal,
                                                     cost_modal, virtual_cache)
        metric = sim.simulate()
        metric.compute()
        print(caching_algorithm_name, metric)
    print('Done')
        # return str(metric)


def test_basic():
    SimulationPlatform().run_simulations(['RR','LFU','LRU','FIFO',], 3, 10000, 10, 1000, 'hit_ratio', 1000, 1.5, None)

def test_all():
    a = caching_algorithms_all
    SimulationPlatform().run_simulations(a, 10,  100000, 10, 1000, ['latency_loss','simple_loss','hit_ratio'], 1000, 1.5, None)
    # SimulationPlatform().run_simulations(a, 1,  10000, 10, 1000, ['latency_loss'], 1000, 1.5, None)
    # SimulationPlatform().run_simulations(['MAD_MIN','MINAD', 'MINAD_W','MINAD_L','MAD_LFU','MIN','MAD','LFU'][:3], 3,  10000, 10, 1000, ['latency_loss'], 1000, 1.1, 839284)

def batch_run_mad():
    # zlist = [1,3.593813664,12.91549665,46.41588834,166.8100537,599.4842503,2154.43469,7742.636827,27825.59402,100000]
    zlist = [12.91549665]
    for z in zlist:
        SimulationPlatform().run_simulations(['MAD_P','MAD'], 3,  100000, 100, 1000, ['latency_loss','simple_loss'], z, 1.5, None)

def test_fixed():
    s = SimulationPlatform().run_simulations(['RR', 'FIFO', 'LRU', 'LFU', 'LFU_IDEAL', 'MAD','MIN','MINAD'],
                                             n_iter=3,
                                             n_requests=999,
                                             cache_size=10,
                                             library_size=1000,
                                             performance_metric_names=['hit_ratio','latency_loss','simple_loss'],
                                             request_frq=1000,
                                             zipf_eta=1.5,
                                             seed = 6748329)

def test_wsweep():
    s = SimulationPlatform().temp(n_iter=5,
                                  n_requests=10000,
                                  cache_size=10,
                                  library_size=1000,
                                  performance_metric_names=['hit_ratio','latency_loss','simple_loss'],
                                  request_frq=1000,
                                  zipf_eta=1.5,
                                  seed = None)
    # print(s)
    # print('+--------------+----------------+-------------+\n| Algorithms   |   latency_loss |   hit_ratio |\n+==============+================+=============+\n| MINAD        |        285.497 |    0.841416 |\n+--------------+----------------+-------------+\n| LFU_IDEAL    |        300.756 |    0.766223 |\n+--------------+----------------+-------------+\n| MAD          |        305.275 |    0.764024 |\n+--------------+----------------+-------------+\n| LFU          |        309.287 |    0.751925 |\n+--------------+----------------+-------------+\n| MIN          |        365.947 |    0.836016 |\n+--------------+----------------+-------------+\n| LRU          |       1059.59  |    0.673833 |\n+--------------+----------------+-------------+\n| RR           |       1422.66  |    0.60244  |\n+--------------+----------------+-------------+\n| FIFO         |       1442.42  |    0.605039 |\n+--------------+----------------+-------------+')
    # if s=='+--------------+----------------+-------------+\n| Algorithms   |   latency_loss |   hit_ratio |\n+==============+================+=============+\n| MINAD        |        285.497 |    0.841416 |\n+--------------+----------------+-------------+\n| LFU_IDEAL    |        300.756 |    0.766223 |\n+--------------+----------------+-------------+\n| MAD          |        305.275 |    0.764024 |\n+--------------+----------------+-------------+\n| LFU          |        309.287 |    0.751925 |\n+--------------+----------------+-------------+\n| MIN          |        365.947 |    0.836016 |\n+--------------+----------------+-------------+\n| LRU          |       1059.59  |    0.673833 |\n+--------------+----------------+-------------+\n| RR           |       1422.66  |    0.60244  |\n+--------------+----------------+-------------+\n| FIFO         |       1442.42  |    0.605039 |\n+--------------+----------------+-------------+':
    #     print('PASS!')
    # else:
    #     print('FAIL!')


# def test():
#     # # a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
#     # a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
#     # b = ['MAD','MAD_P','MIN','MINAD_P']
#     # c = a
#     # SimulationPlatform().run_simulations(c, 2, 10000, 10, 100, ['kappa_ratio', 'hit_ratio','latency_loss'], 1000, 1.5, 2313)
#
#     SimulationPlatform().run_simulations(['MINAD','MINAD2','MAD_MIN','MAD_LFU2','MAD_LFU','LFU','MAD','MIN','MAD_P'],
#                                          n_iter=1,
#                                          n_requests=10000,
#                                          cache_size=10,
#                                          library_size=1000,
#                                          performance_metric_names=['latency_loss','hit_ratio'],
#                                          request_frq=1000,
#                                          zipf_eta=1.5,
#                                          seed = None)

def test_multiple():
    # seed = np.random.randint(2**31)
    # a = caching_algorithms_all
    a = ['MINAD','MIN','MINAD_L','MINAD_W','MAD']
    tabs = dict()
    for x in np.arange(1.1,1.6,0.1):
        r, s = SimulationPlatform().run_simulations(a, 10,  100000, 100, 1000, ['latency_loss'], 1000, x, None)
        tabs[x] = s

    print('#'*100+'\n')

    for c,t in tabs.items(): print(f'# {c}\n',t)

if __name__ == '__main__':
    # batch_run_mad()
    test_wsweep()
    # test()
    # test_multiple()
    # test_online_algorithms()
    # test_offline_algorithms()
    # test_all()