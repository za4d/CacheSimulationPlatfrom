import numpy as np
# from src import *
import performance_metrics
import caching_algorithms
import request_modals
import cost_modals
import simulation_instance
from virtual_cache import VirtualCache


def test():
    # ca = caching_algorithms.FirstInFirstOut(m)
    # ca = caching_algorithms.FirstInLastOut(m)
    # ca = caching_algorithms.LeastFrequentlyUsed(m)
    # ca = caching_algorithms.LeastFrequentlyUsedIdeal(m)
    # ca = caching_algorithms.LeastRecentlyUsed(m)
    a = test_algorithm()
    b = test_algorithm2()
    print(a,b)

def test_algorithm():
    c = 10
    n = 1000
    r = 10000
    # seed = 123
    # np.random.seed(seed)
    vc = VirtualCache(c)
    rm = request_modals.Zipfian(1.7,r,n)
    cm = cost_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
    ###
    ca = caching_algorithms.MinimumAggregateDelay_Perturbed(c,cm,rm)
    ###
    pm = performance_metrics.HitRatio(rm, vc)
    sim = simulation_instance.SimulationInstance(ca, pm, rm, cm, vc)
    metric = sim.simulate()
    metric.compute()
    print(metric)
    print('Done')
    return str(metric)

def test_algorithm2():
    m = 10
    n = 1000
    r = 10000
    # seed = 123
    # np.random.seed(seed)
    vc = VirtualCache(m)
    rm = request_modals.Zipfian(1.7,r,n)
    pm = performance_metrics.HitRatio(rm, vc)
    cm = cost_modals.StaticCost({file: abs(np.random.normal(100, 10)) for file in range(n)})
    ###
    ca = caching_algorithms.Beladys(m,cm,rm)
    ###
    sim = simulation_instance.SimulationInstance(ca, pm, rm, cm, vc)
    metric = sim.simulate()
    metric.compute()
    print(metric)
    print('Done')
    return str(metric)

if __name__ == "__main__":
    test()