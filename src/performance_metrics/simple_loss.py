from performance_metrics import PerformanceMetric


class SimpleLoss(PerformanceMetric):

    @property
    def name(self):
        return 'Simple Loss'

    def __init__(self, request_sequence, initial_state, cost_modal):
        super().__init__(request_sequence, initial_state, cost_modal)
        self.simple_loss = 0


    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        if not self.is_hit(replacement_address):
            self.hit()
            requested_file = self.request_sequence[time]
            self.simple_loss += self.cost(requested_file)

    def __str__(self):
        return f'{self.result :4f}'

    # Loss
    def compute(self):
        self.result = self.simple_loss / (len(self.request_sequence))

    @property
    def params(self):
        return None