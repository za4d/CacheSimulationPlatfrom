from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class CostModal(ABC):

    def __init__(self, library_size):
        self.library_size = library_size

    @abstractmethod
    def cost(self, file):
        pass

    @property
    @abstractmethod
    def params(self):
        """:return true of false, depending on policy type"""
        pass

    def __len__(self):
        return self.library_size


class StaticCost(CostModal, ABC):

    def __init__(self, dict):
        super().__init__(len(dict))
        self.cost_func = dict

    def cost(self, file):
        return self.cost_func[file]

    def asdict(self):
        return self.cost_func

    @property
    def params(self):
        return None