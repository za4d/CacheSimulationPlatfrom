from src.request_modals._request_modal import RequestModal
import numpy as np


class Gaussian(RequestModal):


    def __init__(self, length, library_size, mean=None, std=None):
        super().__init__()
        self._length = length
        self.library_size = library_size
        if mean is None:
            self.mean = library_size//2
            self.std = library_size//20
        else:
            self.std = std
            self.mean = mean

    def _generate(self):
        self.time = 0
        while self.time < self.length:
            request = np.random.normal(self.mean, self.std)
            if request > 0 and request < self.library_size:
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

