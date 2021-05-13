# from .performance_metrics._performance_metric import PerformanceMetric
# from s. import PerformanceMetric
import performance_metrics
from virtual_cache import VirtualCache


class Recorder:

    def __init__(self):
        pass

    def start(self, request_sequence, initial_virtual_cache, cost_modal):
        self.hit_count_ = 0
        self.cost_modal = cost_modal
        self.request_sequence = request_sequence
        self.initial_cache_state = initial_virtual_cache.copy()
        self.simulation_record = []

    def record(self, time, replacement_address):
        if self.is_hit(replacement_address):
            self.hit()
        """time can be used to get requested file from request sequence"""
        self.simulation_record.append((time, self.request_sequence[time], replacement_address))

    def get_performances(self, performance_metric_names):
        cache = VirtualCache(self.initial_cache_state)
        performance_metric_list = [performance_metrics.get(name, self.request_sequence, self.initial_cache_state.copy(), self.cost_modal) for name in performance_metric_names]
        self.goal = performance_metric_list[0].goal

        for time, file, replacement_address in self.simulation_record:
            if replacement_address is not None:
                cache.write(replacement_address, file)
            for pm in performance_metric_list:
                pm.record(time, replacement_address)

        for pm in performance_metric_list:
            pm.compute()

        return performance_metric_list
    
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