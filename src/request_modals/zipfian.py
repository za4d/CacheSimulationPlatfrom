from _request_modal import RequestModal
import numpy as np

class Zipfian(RequestModal):

    def __init__(self, eta, length, library_size):
        self.library_size = library_size
        self._length = length
        self.eta = eta
        super().__init__()


    # '''Generator function that produces a fixed series of random requests'''
    # def _generate(self):
    #     for time, request in zip(range(self._length), np.random.zipf(self.eta, self._length)):
    #         yield (time, request)

    '''Generator function that produces a fixed series of random requests'''
    def _generate(self):
        time = 0
        while time != self.length:
            time += 1
            request = np.random.zipf(self.eta)
            if request < self.library_size:
                yield (time, request)