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

    def __iter__(self):
        return iter(self._request_sequence.items())

    # def __next__(self):
    #     yield next(self._request_sequence.items())
        # items = self._request_sequence.items()
        # for time, file in items:
        #     yield time, file

    def is_hit(self, replacement_address):
        """If file is in cache then return `None` for cache hit. If files is a miss but not cached return -1"""
        return replacement_address is None

    @property
    def length(self):
        return self._length