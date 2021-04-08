from abc import ABC, abstractmethod
from sortedcontainers import SortedDict


class CommunicationModal(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cost(self, file, src=None, dst=None):
        pass
