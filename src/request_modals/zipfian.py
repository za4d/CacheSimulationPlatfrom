from _request_modal import RequestModal
import numpy as np

class Zipfian(RequestModal):

    def __init__(self, eta, length, library_size, seed=None):
        np.random.seed(seed)
        self.library_size = library_size
        self._length = length
        self.eta = eta
        self.time = 0
        super().__init__()


    '''Generator function that produces a fixed series of random requests'''
    def _generate(self):
        for time, request in zip(range(self._length), np.random.zipf(self.eta, self._length)):
            yield (time, request)

