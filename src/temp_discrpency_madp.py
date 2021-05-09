from unittest import TestCase
import numpy as np
import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
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
        cm = cost_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
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
        # cost_modal = cost_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
        cost_modal = cost_modals.StaticNormalCost(library_size, 100, 10)
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
    SimulationPlatform().run_simulations(a, 10,  10000, 100, 10000, 'latency_loss', 1000, 1.5, None)
    SimulationPlatform().run_simulations(a, 10,  10000, 100, 10000, 'hit_ratio', 1000, 1.5, None)

def test():
    # a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
    a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
    b = ['MAD','MAD_P','MIN','MINAD_P']
    c = a
    SimulationPlatform().run_simulations(c, 2, 10000, 2, 1000, ['kappa_ratio', 'hit_ratio','latency_loss'], 1000, 1.5, None)
    # SimulationPlatform().run_simulations(c, 2, 10000, 2, 1000, 'kappa_ratio', 1000, 1.5, None)
    # SimulationPlatform().run_simulations(c, 2, 10000, 2, 1000, 'hit_ratio', 1000, 1.5, None)
    # SimulationPlatform().run_simulations(c, 2, 10000, 2, 1000, 'latency_loss', 1000, 1.5, None)


if __name__ == '__main__':
    test()
    # test_online_algorithms()
    # test_offline_algorithms()
    # test_all()