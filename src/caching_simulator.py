import argparse
import sys
from dataclasses import asdict
from tabulate import tabulate
import numpy as np

from simulation_platform import SimulationPlatform
from utils import Logger, log

import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
import simulation_instance
from virtual_cache import VirtualCache


def run():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='caching-simulator', description='Simulate a caching algorithm.')
    parser.add_argument('--log', metavar='LOG_FILE', type=str, default='logfile.log',
                        help='File name to log terminal output to')

    subparsers = parser.add_subparsers(help='choose run mode', dest='mode')

    # create the parser for the "a" command
    parser_run = subparsers.add_parser('run', help='run basic simulation')
    parser_run.add_argument('ALGORITHMS', nargs='*', choices=caching_algorithms.caching_algorithms_names,
                            type=str.upper, default='-ALL',
                            help=f'List of algorithms to be simulated from {", ".join(caching_algorithms.caching_algorithms_names[:-1])}')
    parser_run.add_argument('-pm', metavar='PERFORMANCE_METRIC', choices=performance_metrics.performance_metrics_names,
                            type=str.lower, default='hit-ratio', help='Measure to track')
    parser_run.add_argument('-cs', metavar='SIZE_OF_CACHE', type=int, default=100, help='Size of the cache memory')
    parser_run.add_argument('-ls', metavar='SIZE_OF_LIBRARY', type=int, default=10000,
                            help='Number of files in main memory')
    parser_run.add_argument('-r', metavar='NUM_OF_REQUESTS', type=int, default=100000,
                            help='Number of requests to be simulated')
    parser_run.add_argument('-i', metavar='NUM_OF_ITERATIONS', type=int, default=10,
                            help='Number of simulations to average results over')
    parser_run.add_argument('-rf', metavar='REQUEST_FREQUENCY', type=float, default=1000,
                            help='Avg. number of requests arriving during a fetch')
    parser_run.add_argument('-e', metavar='ZIPF_ETA', type=float, default=1.5,
                            help='Parameter for the skewness of the distribution')
    parser_run.add_argument('--seed', metavar='SEED', type=int, default=np.random.randint(0, 1000000),
                            help='Seed for request sequence and file cost generation')

    # create the parser for the "b" command
    parser_batch = subparsers.add_parser('batch', help='run simulation batch file (for advanced users)')
    parser_batch.add_argument('BATCH_FILE', metavar='BATCH_FILE', type=str,
                              help='path to batch job description file')

    # # parse some argument lists
    #
    # parser.parse_args(['--foo', 'b', '--baz', 'Z'])
    # args = dict(vars(parser.parse_args()))
    args = parser.parse_args()

    sys.stdout = Logger(args.log)

    # log hyperparameters of simulation instance
    # log(f'>>> HYPERPARAMETERS \nTesting algorithms {str(args.ALGORITHMS).strip("[]")}, {args.i} simulations '
    #     f'of {args.r} requests distributed with eta={args.e}, Cache size is {args.cs} with {args.ls} files in main memory')
    # log(tabulate(tabular_data=list(map(list, args.items())), tablefmt='simple'))

    if args.mode == 'batch':
        print(args.BATCH_FILE)
    elif args.mode == 'run':
        sim = SimulationPlatform.run_simulations(algorithms=args.ALGORITHMS,
                                                 n_iter=args.i,
                                                 n_requests=args.r,
                                                 cache_size=args.cs,
                                                 library_size=args.ls,
                                                 performance_metric_name=args.pm,
                                                 request_frq=args.rf,
                                                 zipf_eta=args.e,
                                                 seed=args.seed)

        print(f'(saved at {args.log})')


if __name__ == "__main__":
    run()
