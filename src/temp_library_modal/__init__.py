import pkgutil
import inspect
from ._library_modal import LibraryModal, CostModel
from .cost_normal import StaticNormalCost
from .cost_uniform import StaticUniformCost


def get(name, *args):
    if name == 'static_normal_cost':
        return StaticNormalCost(*args)
    elif name == 'static_uniform_cost':
        return StaticUniformCost(*args)
    # elif name == 'simpleloss':
    #     return SimpleLoss()
    else:
        raise AttributeError(f'Invalid cost modal name given \'{name}\'')


# Dynamic import files
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)