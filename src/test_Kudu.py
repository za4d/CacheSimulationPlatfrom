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


def test_all(log_file='logfile.log', csv_file='results_log.csv'):
    a = caching_algorithms_all
    SimulationPlatform(log_file=log_file,csv_file=csv_file).run_simulations(a, 10,  10000, 10, 1000, 'latency_loss', 1000, 1.5, None)
    SimulationPlatform(log_file=log_file,csv_file=csv_file).run_simulations(a, 10,  10000, 10, 1000, 'hit_ratio', 1000, 1.5, None)

if __name__ == '__main__':
    test_all(log_file='all3.log', csv_file='all3.csv')