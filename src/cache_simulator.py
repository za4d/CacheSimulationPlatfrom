import numpy as np
# from src import *
import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
import simulation_instance
from virtual_cache import VirtualCache


def test():
    m = 10
    n = 1000
    r = 10000
    vc = VirtualCache(m)
    np.random.seed(100)
    # ca = caching_algorithms.FirstInFirstOut(m)
    ca = caching_algorithms.RandomReplacement(m)
    # ca = caching_algorithms.FirstInLastOut(m)
    # ca = caching_algorithms.LeastFrequentlyUsed(m)
    # ca = caching_algorithms.LeastFrequentlyUsedIdeal(m)
    # ca = caching_algorithms.LeastRecentlyUsed(m)
    rm = request_modals.Zipfian(1.7,r,n)
    pm = performance_metrics.HitRatio(rm, vc)
    cm = cost_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
    sim = simulation_instance.SimulationInstance(ca, pm, rm, cm, vc)
    results = sim.simulate()
    results.compute()
    print(results)
    print('Done')


if __name__ == "__main__":
    test()