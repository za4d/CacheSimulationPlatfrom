from _performance_metric import PerformanceMetric

class SimpleLoss(PerformanceMetric):

    def __init__(self, cost_func, hit_count=0, miss_count=0, hit_weight=1, miss_weight=1):
        self.result = None
        self.processing_time = 10
        self.file_requests_log = dict()
        self.simple_loss = 0
        self.hit_count = self.miss_count = 0
        self.cost_func = cost_func #{file: abs(np.random.normal(10, 30)) for file in self.request_log.keys()}

    @property
    def name(self):
        return 'Simple Loss'

    def __str__(self):
        return f'{self.calculate() :4f}'

    def hit(self, requested_file):
        self.hit_count += 1


    def miss(self, requested_file):
        self.miss_count += 1
        self.simple_loss += self.cost_func[requested_file]

    # Loss
    def compute(self):
        return self.simple_loss / (self.hit_count + self.miss_count)