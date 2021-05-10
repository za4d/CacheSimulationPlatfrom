from abc import ABC, abstractmethod



class OnlineCachingAlgorithm(ABC):
    """If file is in cache then return `None` for no replacment address. If files is not cached but not stored return -1"""

    def __init__(self, cache_size, cost_modal):
        self.cache_size = cache_size
        self.cost_modal = cost_modal

    @abstractmethod
    def __call__(self, time, request, cache_state):
        """:returns replacement address. If file is not going to be cached return`-1` = """
        # if request in cache_state:
        # if is_hit:
        #     # hit
        # else:
        #     # miss
        pass

    @staticmethod
    def online():
        """:return true of false, depending on policy type"""
        return True

    # @property
    # def coded(self):
    #     """:return true of false, depending on policy type"""
    #     return False

    @property
    @abstractmethod
    def params(self):
        """:return a list of object parameters (excluding parent class parameters)"""
        pass


class OfflineCachingAlgorithm(ABC):

    def __init__(self, cache_size, cost_modal, request_sequence):
        self.request_sequence = request_sequence
        self.cost_modal = cost_modal
        self.cache_size = cache_size

    # TODO: cleaner check proprties
    # @classmethod
    # def __init_subclass__(cls):
    #     required_class_variables = [
    #         "online",
    #         "coded"
    #         ""
    #     ]
    #     for var in required_class_variables:
    #         if not hasattr(cls, var):
    #             raise NotImplementedError(
    #                 f'Class {cls} lacks required `{var}` class attribute'
    #             )

    @abstractmethod
    def __call__(self, time, request, cache_state):
        # if request in cache_state:
        # if is_hit:
        #     # hit
        # else:
        #     # miss
        pass

    @staticmethod
    def online():
        """:return true of false, depending on policy type"""
        return False

    # @property
    # def coded(self):
    #     """:return true of false, depending on policy type"""
    #     pass


    @property
    @abstractmethod
    def params(self):
        """:return a list of object parameters (excluding parent class parameters)"""
        pass
