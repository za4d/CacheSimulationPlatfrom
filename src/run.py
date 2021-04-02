import sys
import argparse
from typing import List

import simulation_platform
from tabulate import tabulate
from dataclasses import asdict, dataclass

# from util.logger import Logger

caching_algorithms = ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MIN', 'MAD', 'MAD-P', 'MINAD', 'MINAD-P', 'MINAD-L']  # RR FIFO FILO LRU LFU B
metrics = ['hit-ratio', 'gain', 'loss']

def log(*param):
    print(*param)

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
    HIT_WEIGHT: float
    MISS_WEIGHT: float
    SEED: int
    LOG_FILE: str
    QUITE: bool




def cross_join_args (*seqs):
    if not seqs:
        return [[]]
    else:
        l, ls = seqs[0], seqs[1:]
        if not l:
            l = [[]]
        return [[x] + p for x in l for p in cross_join_args(*ls)]

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Simulate a caching algorithm.')
    # parser.add_argument('ALGORITHMS', nargs='+', choices=caching_algorithms, type=str.upper, help=f'List of algorithms to be simulated from {", ".join(caching_algorithms[:-1])}')
    # parser.add_argument('--metric','--mmmm', nargs='*', nargs='*', metavar='PERFORMANCE_METRIC', default=[], type=str.lower, help='Measure to track')
    # parser.add_argument('--req_modal','-rm', nargs='*', metavar='REQUEST_MODAL', default=[], type=str.lower, help='Measure to track')
    # parser.add_argument('--lib_modal','-lm', nargs='*', metavar='REQUEST_MODAL', default=[], type=str.lower, help='Measure to track')
    # parser.add_argument('-iter','-i', nargs='*', metavar='NUM_OF_ITERATIONS', default=[], type=int, help='Number of simulations to average results over')
    # parser.add_argument('--req_n', '-r', nargs='*', metavar='NUM_OF_REQUESTS', default=[], type=int, help='Number of requests to be simulated')
    # parser.add_argument('-z', nargs='*', metavar='Z', default=[], type=float, help='Avg. number of requests arriving during a fetch')
    # parser.add_argument('--eta', '-e', nargs='*', metavar='ETA', default=[], type=float, help='Parameter for the skewness of the distribution')
    # parser.add_argument('--cache_size', '-c', nargs='*', metavar='SIZE_OF_CACHE', default=[], type=int, help='Size of the cache storage')
    # parser.add_argument('--lib_size', '-l', nargs='*', metavar='SIZE_OF_LIBRARY', default=[], type=int, help='Number of files in library')
    # parser.add_argument('--hit_weight','-hw', nargs='*', metavar='HIT_WEIGHT', default=[], type=float, help='weighting for hits in gain')
    # parser.add_argument('--miss_weight','-mw', nargs='*', metavar='MISS_WEIGHT', default=[], type=float, help='weighting for misses in gain')
    # parser.add_argument('--logfile','-f', nargs='*', metavar='LOG_FILE', default=[], type=str, help='File name to log terminal output to')
    # parser.add_argument('--seed', nargs='*', metavar='SEED', default=[], type=int, help='Seed for request sequence and file cost generation')
    # parser.add_argument('-q', action='store_true', default=False, help='File name to log terminal output to')
    parser = argparse.ArgumentParser(description='Simulate a caching algorithm.')
    parser.add_argument('ALGORITHMS', nargs='*', choices=caching_algorithms, type=str.upper, default='-ALL', help=f'List of algorithms to be simulated from {", ".join(caching_algorithms[:-1])}')
    parser.add_argument('-p', nargs='*', metavar='PERFORMANCE_METRIC', choices=metrics, type=str.lower, default=['hit-ratio'], help='Measure to track')
    parser.add_argument('-i', nargs='*', metavar='NUM_OF_ITERATIONS', type=int, default=[10], help='Number of simulations to average results over')
    parser.add_argument('-r', nargs='*', metavar='NUM_OF_REQUESTS', type=int, default=[100000], help='Number of requests to be simulated')
    parser.add_argument('-z', nargs='*', metavar='Z', type=float, default=[100], help='Avg. number of requests arriving during a fetch')
    parser.add_argument('-e', nargs='*', metavar='ETA', type=float, default=[1.5], help='Parameter for the skewness of the distribution')
    parser.add_argument('-c', nargs='*', metavar='SIZE_OF_CACHE', default=[100], type=int, help='Size of the cache memory')
    parser.add_argument('-m', nargs='*', metavar='SIZE_OF_MAIN', default=[10000], type=int, help='Number of files in main memory')
    parser.add_argument('-hw', nargs='*', metavar='HIT_WEIGHT', type=float, default=[1], help='weighting for hits in gain')
    parser.add_argument('-mw', nargs='*', metavar='MISS_WEIGHT', type=float, default=[1], help='weighting for misses in gain')
    parser.add_argument('--seed', nargs='*', metavar='SEED', type=int, default=[None], help='Seed for request sequence and file cost generation')
    parser.add_argument('-q', action='store_true', default=False, help='File name to log terminal output to')
    parser.add_argument('-f', nargs='*', metavar='LOG_FILE', type=str, default='logfile.log', help='File name to log terminal output to')

    args = list(vars(parser.parse_args()).values())
    # quite = args[-1]
    # logfile = args[-2]
    # hyperparam_list = cross_join_args(*args[:-2])

    sim = simulation_platform.Simulation(args)


