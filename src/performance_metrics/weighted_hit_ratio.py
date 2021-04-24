from _performance_metric import PerformanceMetric

class WeightedHitRatio(PerformanceMetric):

    @property
    def name(self):
        return 'Weighted Hit Ratio'

    def __init__(self, hit_weight=1, miss_weight=1):
        self.hit_weight = hit_weight
        self.miss_weight = miss_weight

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if self.is_hit(replacement_address):
            self.hit()

    def __str__(self):
        return f'{100 * self.result :4f} %'

    # HIT RATIO
    def compute(self):
        self.result = (self.hit_weight*self.hit_count) / (self.hit_count + self.miss_count)



