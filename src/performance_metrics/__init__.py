import pkgutil
import inspect
from ._performance_metric import PerformanceMetric
from .hit_ratio import HitRatio
from .gain import Gain
from .latency_loss import LatencyLoss
from .simple_loss import SimpleLoss

performance_metrics_names = ['hit-ratio', 'gain', 'loss']

def get(name, *args):
    if name == 'hit-ratio':
        return HitRatio(*args)
    elif name == 'gain':
        return Gain(*args)
    elif name == 'latency-loss':
        return LatencyLoss(*args)
    elif name == 'simple-loss':
        return SimpleLoss(*args)
    else:
        raise AttributeError(f'Invalid performance metric name given \'{name}\'')

# Dynamic import files
__all__ = ['get']
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        if name.startswith('__'): continue
        globals()[name] = value
        __all__.append(name)