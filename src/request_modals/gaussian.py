from request_modals import RequestModal
import numpy as np


class Gaussian(RequestModal):


    def __init__(self, num_requests, library_size, mean=None, std=None):
        super().__init__(num_requests, library_size)
        self.mean = mean if mean else library_size//2
        self.std = std if std else library_size//20

    def _generate(self):
        self.time = 0
        while self.time < self.length:
            request = np.random.normal(self.mean, self.std)
            if 0 < request < self.library_size:
                self.time += 1
                yield (self.time, request)


    # def __iter__(self):
    #     while True:
    #         self.time += 1
    #         request = np.random.zipf(self.eta)
    #         if request < self.library_size:
    #             yield (self.time, request)

    # def t(self):
    #     while True:
    #         request_sequence = []
    #         while len(request_sequence) != self.args.NUM_OF_REQUESTS:
    #             r = np.random.zipf(self.eta)
    #             if r < self.library_size:
    #                 request_sequence.append(r)
    #
    #     yield request_sequence

    @property
    def params(self):
        return ['mean', 'std']


