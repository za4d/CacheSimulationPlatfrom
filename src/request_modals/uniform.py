from src.request_modals._request_modal import RequestModal
import numpy as np

class Uniform(RequestModal):

    def __init__(self, length, library_size):
        self.library_size = library_size
        self._length = length
        super().__init__()

    '''Generator function that produces a fixed series of random requests'''
    def _generate(self):
        timestamps = range(self._length)
        requests = np.random.randint(low=0, high=self.library_size, size=self._length)
        return zip(timestamps,requests)

