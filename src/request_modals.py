import numpy as np

class GuassianRequestModal:

    def __init__(self, num_of_requests):
        self.num_of_requests = num_of_requests

    def requests(self):
        return self.__next_request

    def __next_request(self):
        '''Generator function that produces a fixed series of random requests'''
        # generate the list of appropriately distributed requests and simulate
        while True:
            request_sequence = []
            while len(request_sequence) != self.args.NUM_OF_REQUESTS:
                r = np.random.zipf(self.args.ETA)
                if r < self.args.MEMORY_SIZE:
                    request_sequence.append(r)

            yield request_sequence