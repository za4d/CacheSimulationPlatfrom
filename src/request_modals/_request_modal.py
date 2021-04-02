from abc import ABC, abstractmethod
from sortedcontainers import SortedDict

class RequestModal(ABC):

    def __init__(self):
        self._request_sequence = SortedDict(self._generate())

    @abstractmethod
    def _generate(self):
        """Generator function that produces a fixed series of random requests"""
        pass

    def __setitem__(self, time, request):
        self._request_sequence[time] = request

    def __getitem__(self, time):
        return self._request_sequence[time]

    def get(self, index):
        return list(self._request_sequence.items())[index]

    def request_sequence(self, time):
        return self._request_sequence.items()[:time]

    def __delitem__(self, time):
        del self._request_sequence[time]

    def __len__(self):
        return len(self._request_sequence)

    @property
    def length(self):
        return self._length