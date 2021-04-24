# __all__ = ['CachingAlgorithm','RandomReplacement', 'FirstInFirstOut', 'FirstInLastOut', 'LeastRecentlyUsed', 'LeastFrequentlyUsed', 'Beladays', 'MinimumAggregateDelay', 'MinimumAggregateDelay_Beladys', 'MinimumAggregateDelay_Perturbed', 'MinimumAggregateDelay_L', ]
import pkgutil
import inspect
from ._caching_algorithms import OnlineCachingAlgorithm

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

def get(name):
    if name == 'RR':
        return RandomReplacement(self.params.cost_modal)
    elif name == 'FIFO':
        return FirstInFirstOut(*self.params)
    elif name == 'FILO':
        return FirstInLastOut
    elif name == 'LRU':
        return LeastRecentlyUsed(*self.params)
    elif name == 'LFU':
        return LeastFrequentlyUsed(*self.params)
    elif name == 'MIN':
        return Beladys(*self.params)
    elif name == 'MAD':
        return MinimumAggregateDelay(*self.params)
    # elif name == 'MAD-P':
    # 	return MinimumAggregateDelay_Perturbed(*self.params)
    elif name == 'MINAD':
        return MinimumAggregateDelay_Beladys(*self.params)
    elif name == 'MINAD-P':
        return MinimumAggregateDelay_Perturbed(*self.params)
    elif name == 'MINAD-L':
        return MinimumAggregateDelay_L(*self.params)
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

