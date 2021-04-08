from _performance_metric import PerformanceMetric
# from s. import PerformanceMetric


class HitRatio(PerformanceMetric):

    def __init__(self, hit_count=0, miss_count=0):
        self.hit_count = hit_count
        self.miss_count = miss_count

    @property
    def name(self):
        return 'Hit Ratio'

    def hit(self, requested_file):
        self.hit_count += 1

    def miss(self, requested_file):
        self.miss_count += 1

    def __str__(self):
        return f'{100 * self.calculate() :4f} %'

    # HIT RATIO
    def compute(self):
        return self.hit_count / (self.hit_count + self.miss_count)
