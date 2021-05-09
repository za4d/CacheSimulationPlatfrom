# from .performance_metrics._performance_metric import PerformanceMetric
# from s. import PerformanceMetric
import numpy as np

from performance_metrics import PerformanceMetric

"""
implementaion of hitratio with kohens kappa
"""
class KappaRatio(PerformanceMetric):
    goal = 'max'

    @property
    def name(self):
        return 'Kappa Ratio'

    def __init__(self, request_sequence, initial_cache, cost_modal, hit_count=0):
        super().__init__(request_sequence, initial_cache, cost_modal)
        self.hit_count_ = hit_count
        self.random_hit_count = 0
        self.cache_size = len(initial_cache)

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if self.is_hit(replacement_address):
            self.hit()
            
        # check if random replacement was used
        random_address = np.random.randint(self.cache_size)
        if self.is_hit(random_address):
            self.random_hit_count += 1

    def __str__(self):
        return f'{100 * self.result :4f} %'

    # HIT RATIO
    def compute(self):
        p_algorithm = self.hit_count / (len(self.request_sequence))
        p_chance = self.random_hit_count / (len(self.request_sequence))
        self.result = (p_algorithm - p_chance) / (1 - p_chance)

    @property
    def params(self):
        return ['hit_count']