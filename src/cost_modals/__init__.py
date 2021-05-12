import pkgutil
import inspect
from abc import ABCMeta

from ._cost_modal import CostModal, StaticCost
# from .static_normal_cost import StaticNormalCost
# from .static_uniform_cost import StaticUniformCost

# Dynamic import files
get_cost_modals = dict()
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)
        if type(value)==ABCMeta and issubclass(value, (CostModal)):
            if len(value.__abstractmethods__) > 0:
                continue
            get_cost_modals[value.name] = value

def get(name, *args):
    try:
        return get_caching_algorithm[name](*args)
    except KeyError:
        raise AttributeError(f'Invalid cost modal name given \'{name}\'')