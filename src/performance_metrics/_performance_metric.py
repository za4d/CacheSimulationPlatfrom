from abc import ABC, abstractmethod


class PerformanceMetric(ABC):
    _result = None
    _maximise = None

    @property
    @abstractmethod
    def name(self):
        pass

    def __init__(self, request_sequence, initial_cache, cost_modal):
        self._reverse = None
        self.hit_count_ = 0
        self.cost_modal = cost_modal
        self.initial_cache = initial_cache
        self.request_sequence = request_sequence

    @classmethod
    def __init_subclass__(cls):
        if not hasattr(cls, 'goal'):
            raise NotImplementedError(
                f'Class {cls} lacks required `goal` class attribute'
            )
        elif cls.goal in 'max':
            cls._maximise = True
        elif cls.goal in 'min':
            cls._maximise = False
        else:
            raise ValueError(f'performance metric {cls} `goal ={cls.goal}` not =\'max\' or =\'min\'')

    @abstractmethod
    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        pass

    def logHit(self, time, replacement_address):
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

    @property
    @abstractmethod
    def params(self):
        """:return true of false, depending on policy type"""
        pass

    @property
    def to_maximise(self):
        if self._maximise is None:
            raise AttributeError(f'{self} goal not declared')
        return self._maximise