from _performance_metric import PerformanceMetric


class Gain(PerformanceMetric):

    @property
    def name(self):
        return 'Gain'

    def __init__(self, cost_func, hit_weight=1, miss_weight=1):
        self.hit_weight = hit_weight
        self.miss_weight = miss_weight

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if self.is_hit(replacement_address):
            self.hit()

    def __str__(self):
        return str(self.compute())

    # GAIN
    def compute(self):
        """Returns the 'gain' per request"""
        h = self.hit_weight * self.hit_count
        m = self.miss_count * self.miss_weight
        return (h - m) / (self.hit_count + self.miss_count)
