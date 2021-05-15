from unittest import TestCase
import numpy as np
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


def test_all():
    a = caching_algorithms_all
    SimulationPlatform().run_simulations(a, 10,  100000, 10, 1000, ['latency_loss','simple_loss','hit_ratio'], 1000, 1.5, None)




def test_multiple():
    i,r = 10, 10000
    # i,r = 2, 10
    tabs = dict()
    zs = [np.power(10,p) for p in [0.00001,1,2, 2.33333333, 2.66666667, 3, 3.33333333,3.66666667, 4.,5,6]]
    # zs = [1000,10]

    for z in zs:
        results = SimulationPlatform().run_simulations(caching_algorithms_all, i,  r, 100, 1000, ['hit_ratio', 'latency_loss', 'simple_loss'], 1000, z, None)
        tabs[z] = (results.table_str,results.csv_str,results.headers)

    c = ''
    for z, (tbl,csv,header) in tabs.items():
        print(f'# {z}\n'+tbl)
        c+=csv

    print(header+'\n'+c)

    print('#'*100+'\n')

if __name__ == '__main__':
    test_multiple()
    # test()
    # test_online_algorithms()
    # test_offline_algorithms()