# __all__ = ['CachingAlgorithm','RandomReplacement', 'FirstInFirstOut', 'FirstInLastOut', 'LeastRecentlyUsed', 'LeastFrequentlyUsed', 'Beladays', 'MinimumAggregateDelay', 'MinimumAggregateDelay_Beladys', 'MinimumAggregateDelay_Perturbed', 'MinimumAggregateDelay_L', ]
import pkgutil
import inspect
from abc import ABCMeta

from ._caching_algorithms import CachingAlgorithm, OnlineCachingAlgorithm, OfflineCachingAlgorithm
# from .FirstInLastOut import FirstInLastOut
# from .FirstInFirstOut import FirstInFirstOut
# from .LeastRecentlyUsed import LeastRecentlyUsed
# from .LeastFrequentlyUsed import LeastFrequentlyUsed
# from .LeastFrequentlyUsed_Ideal import LeastFrequentlyUsedIdeal
# from .RandomReplacement import RandomReplacement
# from .Beladys import Beladys
# from .MAD import MAD, TrackAggregateDelay
# from .MinimumAggregateDelay import MinimumAggregateDelay
# from .MinimumAggregateDelayLayered import MinimumAggregateDelayLayered
# from .MinimumAggregateDelayPerturbed import MinimumAggregateDelayPerturbed
# from .MinimumAggregateDelay_Weighted import MinimumAggregateDelayWeighted
# from .MAD_Perturbed import MADPerturbed
# from .MAD_LFU import MAD_LFU, MAD_LFU2
# from .MAD_MIN import MAD_MIN

# Dynamic import files
get_caching_algorithm = dict()
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)
        if type(value)==ABCMeta and issubclass(value, (OfflineCachingAlgorithm, OnlineCachingAlgorithm)):
            if len(value.__abstractmethods__) > 0:
                continue
            get_caching_algorithm[value.name] = value

# print(get_caching_algorithm)
# get_caching_algorithm = {n 	: RandomReplacement
# get_caching_algorithm = {'RR' 	: RandomReplacement,
#                          'FIFO' 	: FirstInFirstOut,
#                          'FILO' 	: FirstInLastOut,
#                          'LRU' 	: LeastRecentlyUsed,
#                          'LFU' 	: LeastFrequentlyUsed,
#                          'LFU_IDEAL' 	: LeastFrequentlyUsedIdeal,
#                          'MIN' 	: Beladys,
#                          'MAD' 	: MAD,
#                          'MAD_LFU' 	: MAD_LFU,
#                          'MAD_P' 	: MADPerturbed,
#                          'MAD_MIN' 	: MAD_MIN,
#                          'MAD_MIN2' 	: MAD_LFU2,
#                          'MINAD' 	: MinimumAggregateDelay,
#                          'MINAD_P' 	: MinimumAggregateDelayPerturbed,
#                          'MINAD_L' 	: MinimumAggregateDelayLayered,
#                          'MINAD_W' 	: MinimumAggregateDelayWeighted
#                          }
caching_algorithms_all = get_caching_algorithm.keys()# RR FIFO FILO LRU LFU B
caching_algorithms_online = [k for k, ca in get_caching_algorithm.items() if ca.online()]
caching_algorithms_offline = [k for k, ca in get_caching_algorithm.items() if not ca.online()]

# def get(name, cache_size, cost_modal, request_sequence):
#     if name == 'RR':
#         return RandomReplacement(cache_size, cost_modal)
#     elif name == 'FIFO':
#         return FirstInFirstOut(cache_size, cost_modal)
#     elif name == 'FILO':
#         return FirstInLastOut(cache_size, cost_modal)
#     elif name == 'LRU':
#         return LeastRecentlyUsed(cache_size, cost_modal)
#     elif name == 'LFU':
#         return LeastFrequentlyUsed(cache_size, cost_modal)
#     elif name == 'MIN':
#         return Beladys(cache_size, cost_modal, request_sequence)
#     elif name == 'MAD':
#         return MinimumAggregateDelay(cache_size, cost_modal)
#     # elif name == 'MAD-P':
#     # 	return MinimumAggregateDelay_Perturbed(*self.params)
#     elif name == 'MINAD':
#         return MinimumAggregateDelay_Beladys(cache_size, cost_modal, request_sequence)
#     elif name == 'MINAD-P':
#         return MinimumAggregateDelay_Perturbed(cache_size, cost_modal, request_sequence)
#     elif name == 'MINAD-L':
#         return MinimumAggregateDelay_L(cache_size, cost_modal, request_sequence)
#     else:
#         raise AttributeError(f'Invalid caching algorithm given \'{name}\'')

def is_online(name):
    name = name.upper()
    if name in caching_algorithms_online:
        return True
    if name in caching_algorithms_offline:
        return False
    else:
        raise ValueError(f'Invalid caching algorithm given \'{name}\'')



def get(name, *args):
    try:
        return get_caching_algorithm[name](*args)
    except KeyError:
        raise ValueError(f'Invalid caching algorithm given \'{name}\'')



