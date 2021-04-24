from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class CostModal(ABC):

    def __init__(self, library_size):
        self.library_size = library_size


    @abstractmethod
    def cost(self, file):
        pass
