from _request_modal import RequestModal
import numpy as np


class Gaussian(RequestModal):


    def __init__(self, mean, std, length, library_size):
        self.std = std
        self.mean = mean
        self._length = length
        self.library_size = library_size
        super().__init__()


    def _generate(self):
        self.time = 0
        while self.time < self.length:
            self.time += 1
            request = np.random.normal(self.mean, self.std)
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

