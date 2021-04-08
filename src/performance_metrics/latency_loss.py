from _performance_metric import PerformanceMetric

class LatencyLoss(PerformanceMetric):

    def __init__(self, cost_func, hit_count=0, miss_count=0, hit_weight=1, miss_weight=1):
        self.latency_loss = None
        self.processing_time = 10
        self.file_requests_log = dict()
        self.time = 0
        self.hit_count = self.miss_count = 0
        self.cost_func = cost_func #{file: abs(np.random.normal(10, 30)) for file in self.request_log.keys()}


    @property
    def name(self):
        return 'Latency Loss'

    def __str__(self):
        return f'{self.calculate() :4f}'

    def hit(self, requested_file):
        self.hit_count += 1
        log_entry = (self.time, True)
        self.time += 1
        try:
            self.file_requests_log[requested_file].append(log_entry)
        except KeyError:
            self.file_requests_log[requested_file] = [log_entry]


    def miss(self, requested_file):
        self.miss_count += 1
        log_entry = (self.time, False)
        self.time += 1
        try:
            self.file_requests_log[requested_file].append(log_entry)
        except KeyError:
            self.file_requests_log[requested_file] = [log_entry]

    # Loss
    def compute(self):
        if self.latency_loss:
            return self.latency_loss

        latency_loss = 0
        for file, request_history in self.file_requests_log.items():
            c = self.cost_func[file]
            try:
                # skip any cache hits from file being in initial cache
                while True:
                    r0_t, r0_is_hit = request_history.pop(0)
                    # find delayed hits of cache miss request r0
                    if not r0_is_hit:
                        window = r0_t + c
                        delayed_hits = [r0_t]
                        # get all request inside the fetch window of r0
                        while request_history:
                            t, cache_hit = request_history.pop(0)
                            if t > window:
                                # Add back request that was outside the window
                                request_history.insert(0,(t, cache_hit))
                                break
                            else:
                                delayed_hits.append(t)

                        # Calculate latency loss
                        processing_delay = self.processing_time * sum(range(len(delayed_hits)))
                        queueing_delay = len(delayed_hits) * (c + r0_t) - sum(delayed_hits)
                        latency_loss += processing_delay + queueing_delay

            except IndexError:
                pass

        self.latency_loss = latency_loss / self.time
        return self.latency_loss