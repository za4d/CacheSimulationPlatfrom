__all__ = ['Results','Logger','log']

from .results import Results
from .logger import Logger

def log(*param):
    print(*param)