import pkgutil
import inspect
from ._cost_modal import CostModal
# from static_cost import StaticCost


def get(name, **args):
    if name == 'static-cost':
        return StaticCost(**args)
    # elif name == 'simpleloss':
    #     return SimpleLoss()
    else:
        raise AttributeError(f'Invalid request modal name given \'{name}\'')


# Dynamic import files
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)