from unittest import TestCase
import numpy as np
import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
import simulation_instance
from simulation_platform import SimulationPlatform
from virtual_cache import VirtualCache

a_online = ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MAD']
a_offline = ['MIN', 'MINAD', 'MINAD_P', 'MINAD_L']
a_all = ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MAD', 'MIN', 'MINAD', 'MINAD_P', 'MINAD_L']
# class TestAlgorithms(TestCase):
#
#     def t(self):
#         print('Y')


def test_basic():
    SimulationPlatform().run_simulations(['RR','LFU','LRU','FIFO',], 3, 10000, 10, 1000, 'hit_ratio', 1000, 1.5, None)

def test_all(log_file=log_file,csv_file=csv_file):
    a = a_all
    SimulationPlatform(log_file=log_file,csv_file=csv_file).run_simulations(a, 10,  10000, 100, 10000, 'hit_ratio', 1000, 1.5, None)
    SimulationPlatform(log_file=log_file,csv_file=csv_file).run_simulations(a, 10,  10000, 100, 10000, 'latency_loss', 1000, 1.5, None)

def test(log_file='logfile.log', csv_file='results.csv'):
    # a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
    a = ['RR', 'FIFO', 'LRU', 'LFU', 'MAD']
    SimulationPlatform().run_simulations(a, 2, 1000, 10, 10000, 'hit_ratio', 1000, 1.5, None)
    # SimulationPlatform().run_simulations(a, 2, 1000, 10, 1000, 'hit_ratio', 1000, 1.5, 9909739)

if __name__ == '__main__':
    # test()
    # test_online_algorithms()
    # test_offline_algorithms()
    test_all(log_file='all1.log', csv_file='all1.csv')