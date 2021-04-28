from request_modals import RequestModal
import numpy as np

class Uniform(RequestModal):

    def __init__(self, num_requests, library_size):
        super().__init__(num_requests, library_size)

    '''Generator function that produces a fixed series of random requests'''
    def _generate(self):
        timestamps = range(self.length)
        requests = np.random.randint(low=0, high=self.library_size, size=self.length)
        return zip(timestamps,requests)

    @property
    def params(self):
        return None