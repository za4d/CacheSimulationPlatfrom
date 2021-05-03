from tabulate import tabulate

class Results(dict):

    def __init__(self, algorithms, n_iter, n_requests, cache_size, library_size, performance_metric_name, request_frq, zipf_eta, seed):
        super().__init__({a: None for a in algorithms})
        self.algorithms = algorithms
        self.n_iter = n_iter
        self.n_requests = n_requests
        self.cache_size = cache_size
        self.library_size = library_size
        self.performance_metric_name = performance_metric_name
        self.request_frq = request_frq
        self.zipf_eta = zipf_eta
        self.seed = seed

    def __str__(self):
        headers, data = self.csv()
        return f'{headers}\n{data}'

    def csv(self):
        headers = 'ALGORITHM,METRIC,RESULT,REQUEST_FRQ,ZIPF_ETA,N_ITER,N_REQUESTS,CACHE_SIZE,LIBRARY_SIZE,SEED'
        data = ''
        for algorithm, result in self.items():
            data += f'{algorithm},{self.performance_metric_name},{result},{self.request_frq},{self.zipf_eta},{self.n_iter},{self.n_requests},{self.cache_size},{self.library_size},{self.seed} \n'
        return headers, data #.rstrip("\n")

    def table(self, sort=False):
        if sort:
            data = sorted(self.items(), key=lambda tup: tup[1])
        else:
            data = self.items()

        return tabulate(data,
                        headers = ['Algorithms', f'{self.performance_metric_name} ({self.n_iter})'],
                        tablefmt='github')
