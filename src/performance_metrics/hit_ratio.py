from src.performance_metrics._performance_metric import PerformanceMetric
# from s. import PerformanceMetric


class HitRatio(PerformanceMetric):

    @property
    def name(self):
        return 'Hit Ratio'

    def __init__(self, request_sequence, initial_state, cost_modal, hit_count=0):
        super().__init__(request_sequence, initial_state, cost_modal)
        self.hit_count_ = hit_count

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if self.is_hit(replacement_address):
            self.hit()

    def __str__(self):
        return f'{100 * self.result :4f} %'

    # HIT RATIO
    def compute(self):
        self.result = self.hit_count / (len(self.request_sequence))
