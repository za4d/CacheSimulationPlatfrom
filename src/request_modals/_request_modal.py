from abc import ABC, abstractmethod
from sortedcontainers import SortedDict

class RequestModal(ABC):

    def __init__(self, num_requests, library_size):
        self._length = num_requests
        self._library_size = library_size
        self._request_sequence = SortedDict(self._generate())

    @abstractmethod
    def _generate(self):
        """Generator function that produces a fixed series of random requests"""
        pass

    def time_of_next_request(self, search_file):
        for address, file in self._request_sequence.items():
            if file == search_file:
                return address
        raise ValueError('No request for file in sequence')


    def __setitem__(self, time, request):
        self._request_sequence[time] = request

    def __getitem__(self, time):
        return self._request_sequence[time]

    def get(self, index):
        return list(self._request_sequence.items())[index]

    def request_sequence(self, time=None):
        return self._request_sequence.items()[:time]

    def aslist(self):
        return list(self._request_sequence.values())

    def __delitem__(self, time):
        del self._request_sequence[time]

    def __len__(self):
        return len(self._request_sequence)

    def __iter__(self):
        return iter(self._request_sequence.items())

    def __contains__(self, item):
        return item in self._request_sequence


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

    @property
    def library_size(self):
        return self._library_size

    @property
    @abstractmethod
    def params(self):
        """:return true of false, depending on policy type"""
        pass