from tabulate import tabulate

class Results(dict):
    headers = 'ALGORITHM,METRIC,RESULT,REQUEST_FRQ,ZIPF_ETA,N_ITER,N_REQUESTS,CACHE_SIZE,LIBRARY_SIZE,SEED'

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
        return self.headers, self.data+'\n'

    def table(self, goal=None):
        if goal=='min':
            data = sorted(self.items(), key=lambda tup: tup[1], reverse=False)
        elif goal=='max':
            data = sorted(self.items(), key=lambda tup: tup[1], reverse=True)
        else:
            raise AttributeError('no order specied')


        return tabulate(data,
                        headers = ['Algorithms', f'{self.performance_metric_name} ({self.n_iter})'],
                        tablefmt='github')

    @property
    def data(self):
        d = ''
        for algorithm, result in self.items():
            d += f'{algorithm},{self.performance_metric_name},{result},{self.request_frq},{self.zipf_eta},{self.n_iter},{self.n_requests},{self.cache_size},{self.library_size},{self.seed} \n'
        return d.rstrip("\n")
