import pkgutil
import inspect
from abc import ABCMeta

from ._library_modal import LibraryModel, CostModel, FaultModel, GeneralModel, BitModel
# from .static_normal_cost import StaticNormalCost
# from .static_uniform_cost import StaticUniformCost

# Dynamic import files
get_cost_modals = dict()
__all__ = ['get']
abstact_classes = (LibraryModel, CostModel, FaultModel, GeneralModel, BitModel)
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)
        if inspect.isclass(value):
            if name not in ['LibraryModel', 'CostModel', 'FaultModel', 'GeneralModel', 'BitModel', 'ABC'] and issubclass(value, LibraryModel):
                get_cost_modals[value.name] = value

def get(name, *args):
    try:
        return get_cost_modals[name](*args)
    except KeyError:
        raise AttributeError(f'Invalid cost modal name given \'{name}\'')