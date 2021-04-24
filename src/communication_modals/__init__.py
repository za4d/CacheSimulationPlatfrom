import pkgutil
import inspect

def get(name, **args):
    if name == 'g':
        return Gaussian(**args)
    elif name == 'z':
        return Zipfian(**args)
    elif name == 'u':
        return Uniform(**args)
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