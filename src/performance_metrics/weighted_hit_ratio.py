from _performance_metric import PerformanceMetric

class WeightedHitRatio(PerformanceMetric):

    def __init__(self, hit_count=0, miss_count=0, hit_weight=1, miss_weight=1):
        self.hit_count = hit_count
        self.miss_count = miss_count
        self.hit_weight = hit_weight
        self.miss_weight = miss_weight

    @property
    def name(self):
        return 'Weighted Hit Ratio'


    def hit(self, requested_file):
        self.hit_count += 1

    def miss(self, requested_file):
        self.miss_count += 1

    def __str__(self):
        return f'{100 * self.calculate() :4f} %'

    # HIT RATIO
    def calculate(self):
        return self.hit_count / (self.hit_count + self.miss_count)


