from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class LibraryModal(ABC):

    def __init__(self, library_size):
        self.library_size = library_size

    @abstractmethod
    def cost(self, file):
        pass

    @abstractmethod
    def size(self, file):
        pass

    @property
    @abstractmethod
    def params(self):
        """:return true of false, depending on policy type"""
        pass

    def __len__(self):
        return self.library_size


class CostModel(LibraryModal, ABC):

    def __init__(self, dict):
        super().__init__(len(dict))
        self.cost_func = dict

    def cost(self, file):
        return self.cost_func[file]

    def size(self, file):
        return 1

    @property
    def params(self):
        return None

class FaultModel(LibraryModal, ABC):

    def __init__(self, dict):
        super().__init__(len(dict))
        self.size_func = dict

    def cost(self, file):
        return 1

    def size(self, file):
        return self.size_func[file]

    @property
    def params(self):
        return None

class BitModel(LibraryModal, ABC):

    def __init__(self, dict):
        super().__init__(len(dict))
        self.cost_func = dict

    def cost(self, file):
        return self.cost_func[file]

    def size(self, file):
        return self.cost(file)

    @property
    def params(self):
        return None



class GeneralModel(LibraryModal, ABC):

    def __init__(self, cost_dict, size_dict):
        super().__init__(len(dict))
        self.cost_func = cost_dict
        self.size_func = size_dict

    def cost(self, file):
        return self.cost_func[file]

    def size(self, file):
        return self.size_func[file]

    @property
    def params(self):
        return None
