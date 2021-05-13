from tabulate import tabulate

class Results(dict):
    headers = 'ALGORITHM,METRIC,RESULT,REQUEST_FRQ,ZIPF_ETA,N_ITER,N_REQUESTS,CACHE_SIZE,LIBRARY_SIZE,SEED'

    def __init__(self, algorithms, n_iter, n_requests, cache_size, library_size, performance_metric_names, request_frq, zipf_eta, seed):
        super().__init__({a: {} for a in algorithms})
        self.algorithms = algorithms
        self.n_iter = n_iter
        self.n_requests = n_requests
        self.cache_size = cache_size
        self.library_size = library_size
        self.performance_metric_names = performance_metric_names

        self.request_frq = request_frq
        self.zipf_eta = zipf_eta
        self.seed = seed

    def __str__(self):
        headers, data = self.csv()
        return f'{headers}\n{data}'

    def csv(self):
        d = self.data()
        s = ''
        for tpl in d:
            s += ', '.join(map(str,tpl)) + f'\n'
        s.rstrip("\n")

        return self.headers, s +'\n'

    def table(self, goal=None, tblfmt='github', col=None):
        data = self.data(col=col)

        if goal=='min':
            data = sorted(data, key=lambda tup: tup[1], reverse=False)
        elif goal=='max':
            data = sorted(data, key=lambda tup: tup[1], reverse=True)
        else:
            raise AttributeError('no order specied')

        if col:
            headers = ['Algorithms', self.performance_metric_names[col]]
        else:
            headers = ['Algorithms', *self.performance_metric_names]

        return tabulate(data,
                        headers = headers,
                        tablefmt=tblfmt)


    def data(self, col=None):
        d = [(a, *[result for pm, result in pms.items()]) for a, pms in self.items()]
        if col is None:
            return d
        else:
            return [(t[0],t[col]) for t in d]
