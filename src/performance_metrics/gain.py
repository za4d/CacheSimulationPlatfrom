# from performance_metrics import PerformanceMetric
from performance_metrics import PerformanceMetric

class Gain(PerformanceMetric):
    goal = 'max'

    @property
    def name(self):
        return 'Gain'

    def __init__(self, request_sequence, initial_cache, cost_modal, hit_weight=1, miss_weight=1):
        super().__init__(request_sequence, initial_cache, cost_modal)
        self.hit_weight = hit_weight
        self.miss_weight = miss_weight

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if self.is_hit(replacement_address):
            self.hit()

    def __str__(self):
        return str(self.result)

    # GAIN
    def compute(self):
        """Returns the 'gain' per request"""
        h = self.hit_weight * self.hit_count
        m = self.miss_count * self.miss_weight
        self.result = (h - m) / (self.hit_count + self.miss_count)

    @property
    def params(self):
        return ['hit_weight','miss_weight']