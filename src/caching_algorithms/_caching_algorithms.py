from abc import ABC, abstractmethod



class CachingAlgorithm(ABC):
    """If file is in cache then return `None` for no replacment address. If files is not cached but not stored return -1"""


    @abstractmethod
    def __call__(self, time, request, cache_state):
        """:returns replacement address. If file is not going to be cached return`-1` = """
        # if request in cache_state:
        # if is_hit:
        #     # hit
        # else:
        #     # miss
        pass

    @property
    @abstractmethod
    def online(self):
        """:return true of false, depending on policy type"""
        return True

    @property
    @abstractmethod
    def coded(self):
        """:return true of false, depending on policy type"""
        pass



class OfflineCachingAlgorithm(ABC):

    def __init__(self, request_sequence):
        self._request_sequence = request_sequence

    @abstractmethod
    def __call__(self, cache_state, request, time):
        # if request in cache_state:
        # if is_hit:
        #     # hit
        # else:
        #     # miss
        pass

    @property
    def online(self):
        """:return true of false, depending on policy type"""
        return False

    @property
    @abstractmethod
    def coded(self):
        """:return true of false, depending on policy type"""
        pass



