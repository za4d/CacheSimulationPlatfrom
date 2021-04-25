import pkgutil
import inspect
from ._request_modal import RequestModal
from .gaussian import Gaussian
from .uniform import Uniform
from .zipfian import Zipfian

def get(name, args):
    if name == 'gaussian':
        return Gaussian(*args)
    elif name == 'zipfian':
        return Zipfian(*args)
    elif name == 'uniform':
        return Uniform(*args)
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