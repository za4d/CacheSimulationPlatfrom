from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class CostModal(ABC):

    @abstractmethod
    def cost(self, file):
        pass
