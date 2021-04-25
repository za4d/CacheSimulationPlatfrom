from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class CostModal(ABC):

    def __init__(self, library_size):
        self.library_size = library_size

    @abstractmethod
    def cost(self, file):
        pass


class StaticCost(CostModal):

    def __init__(self, dict):
        super().__init__(len(dict))
        self.cost_func = dict

    def cost(self, file):
        return self.cost_func[file]
