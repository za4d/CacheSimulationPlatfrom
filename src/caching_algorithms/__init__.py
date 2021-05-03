# __all__ = ['CachingAlgorithm','RandomReplacement', 'FirstInFirstOut', 'FirstInLastOut', 'LeastRecentlyUsed', 'LeastFrequentlyUsed', 'Beladays', 'MinimumAggregateDelay', 'MinimumAggregateDelay_Beladys', 'MinimumAggregateDelay_Perturbed', 'MinimumAggregateDelay_L', ]
import pkgutil
import inspect
from ._caching_algorithms import OnlineCachingAlgorithm, OfflineCachingAlgorithm
from .FirstInLastOut import FirstInLastOut
from .FirstInFirstOut import FirstInFirstOut
from .LeastRecentlyUsed import LeastRecentlyUsed
from .LeastFrequentlyUsed import LeastFrequentlyUsed
from .LeastFrequentlyUsed_Ideal import LeastFrequentlyUsedIdeal
from .RandomReplacement import RandomReplacement
from .Beladys import Beladys
from .MinimumAggregateDelay import MinimumAggregateDelay
from .MinimumAggregateDelay_Beladys import MinimumAggregateDelay_Beladys
from .MinimumAggregateDelay_L import MinimumAggregateDelay_L
from .MinimumAggregateDelay_Perturbed import MinimumAggregateDelay_Perturbed

caching_algorithms_names = ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MIN', 'MAD', 'MINAD', 'MINAD-P', 'MINAD-L']  # RR FIFO FILO LRU LFU B

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
    if name in ['RR', 'FIFO', 'FILO', 'LRU', 'LFU', 'MAD']:
        return True
    if name in ['MIN', 'MINAD', 'MINAD_P', 'MINAD_L']:
        return False
    else:
        raise ValueError(f'Invalid caching algorithm given \'{name}\'')

def get(name, *args):
    if name == 'RR':
        return RandomReplacement(*args)
    elif name == 'FIFO':
        return FirstInFirstOut(*args)
    elif name == 'FILO':
        return FirstInLastOut(*args)
    elif name == 'LRU':
        return LeastRecentlyUsed(*args)
    elif name == 'LFU':
        return LeastFrequentlyUsed(*args)
    elif name == 'MIN':
        return Beladys(*args)
    elif name == 'MAD':
        return MinimumAggregateDelay(*args)
    # elif name == 'MAD-P':
    # 	return MinimumAggregateDelay_Perturbed(*self.params)
    elif name == 'MINAD':
        return MinimumAggregateDelay_Beladys(*args)
    elif name == 'MINAD_P':
        return MinimumAggregateDelay_Perturbed(*args)
    elif name == 'MINAD_L':
        return MinimumAggregateDelay_L(*args)
    else:
        raise AttributeError(f'Invalid caching algorithm given \'{name}\'')

# Dynamic import files
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)

