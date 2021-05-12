# from .performance_metrics._performance_metric import PerformanceMetric
# from s. import PerformanceMetric
import performance_metrics


class Record:

    def __init__(self, request_sequence, initial_cache, cost_modal):
        self.cost_modal = cost_modal
        self.request_sequence = request_sequence
        self.initial_state = initial_cache.copy()
        self.simulation_record = []

    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        self.simulation_record.append((time, self.request_sequence[time], replacement_address))

    def get_performances(self, performance_metric_names):
        cache = self.initial_state.copy()
        perfromance_metric_list = [performance_metrics.get(name, self.request_sequence, self.initial_state.copy(), self.cost_modal) for name in performance_metric_names]

        for time, file, replacement_address in self.simulation_record:
            if replacement_address is not None:
                cache.write(replacement_address, file)
            for pm in perfromance_metric_list:
                pm.simulation_record(time, replacement_address)

        return perfromance_metric_list
