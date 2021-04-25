from abc import ABC, abstractmethod


class PerformanceMetric(ABC):
    _result = None

    @property
    @abstractmethod
    def name(self):
        pass

    def __init__(self, request_sequence, initial_state, cost_modal):
        self.hit_count_ = 0
        self.cost_modal = cost_modal
        self.initial_state = initial_state
        self.request_sequence = request_sequence

    @abstractmethod
    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        pass

    @abstractmethod
    def __str__(self):
        """Formatted string representation of metric value"""
        pass

    @abstractmethod
    def compute(self):
        """calculate metric result and set self.result"""
        pass

    def cost(self, file):
        return self.cost_modal.cost(file)

    @property
    def result(self):
        if self._result is None:
            raise NameError('Result not yet computed')
        else:
            return self._result

    @result.setter
    def result(self, result):
        self._result = result


    def is_hit(self, replacement_address):
        """If file is in cache then return `None` for cache hit. If files is a miss but not cached return -1"""
        return replacement_address is None

    def hit(self):
        self.hit_count_ += 1

    @property
    def hit_count(self):
        return self.hit_count_

    @property
    def miss_count(self):
        return len(self.request_sequence) - self.hit_count_

    # @abstractmethod
    # def __add__(self, other):
    #     pass




