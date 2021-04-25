from src.performance_metrics._performance_metric import PerformanceMetric

class LatencyLoss(PerformanceMetric):

    @property
    def name(self):
        return 'Latency Loss'

    def __init__(self, request_sequence, initial_state, cost_modal):
        super().__init__(request_sequence, initial_state, cost_modal)
        self.latency_loss = None
        self.processing_time = 10
        self.file_requests_log = dict()
        self.time = 0
        # self.cost_modal = cost_modal #{file: abs(np.random.normal(10, 30)) for file in self.request_log.keys()}


    def record(self, time, replacement_address):
        """time can be used to get requested file from request sequence"""
        requested_file = self.request_sequence[time]
        if self.is_hit(replacement_address):
            self.hit()
            log_entry = (self.time, True)
            self.time += 1
            try:
                self.file_requests_log[requested_file].append(log_entry)
            except KeyError:
                self.file_requests_log[requested_file] = [log_entry]
        else:
            log_entry = (self.time, False)
            self.time += 1
            try:
                self.file_requests_log[requested_file].append(log_entry)
            except KeyError:
                self.file_requests_log[requested_file] = [log_entry]


    def __str__(self):
        return f'{self.result :4f}'

    # Loss
    def compute(self):
        if self.latency_loss:
            return self.latency_loss

        latency_loss = 0
        for file, request_history in self.file_requests_log.items():
            c = self.cost(file)
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
        self.result = self.latency_loss