from abc import ABC, abstractmethod


class PerformanceMetric(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def __str__(self):
        """Formatted string representation of metric value"""
        pass

    @abstractmethod
    def hit(self, requested_file):
        """What to do in the event of a cache hit"""
        pass

    @abstractmethod
    def miss(self, requested_file):
        """What to do in the event of a cache miss"""
        pass

    @abstractmethod
    def compute(self):
        """calculate metric result"""
        pass

    @abstractmethod
    def __add__(self, other):
        pass
