from _performance_metric import PerformanceMetric


class Gain(PerformanceMetric):

    def __init__(self, cost_func, hit_count=0, miss_count=0, hit_weight=1, miss_weight=1):
        self.hit_count = hit_count
        self.miss_count = miss_count
        self.hit_weight = hit_weight
        self.miss_weight = miss_weight

    @property
    def name(self):
        return 'Gain'

    def hit(self, requested_file):
        self.hit_count += 1

    def miss(self, requested_file):
        self.miss_count += 1

    def __str__(self):
        return str(self.calculate())

    # GAIN
    def calculate(self):
        """Returns the 'gain' per request"""
        return (self.hit_weight*self.hit_count - self.miss_count*self.miss_weight) / (self.hit_count + self.miss_count)
