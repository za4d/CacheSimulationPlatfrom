from tabulate import tabulate

class Results(dict):

    def __init__(self, algorithms, n_iter, n_requests, cache_size, library_size, performance_metric_names, request_frq, zipf_eta, seed):
        super().__init__({a: {} for a in algorithms})
        self.algorithms = algorithms
        self.performance_metric_names = performance_metric_names
        self.request_frq = request_frq
        self.zipf_eta = zipf_eta
        self.n_iter = n_iter
        self.n_requests = n_requests
        self.cache_size = cache_size
        self.library_size = library_size
        self.seed = seed
        self.headers = 'ALGORITHM,'+','.join(map(str.upper,performance_metric_names))+',REQUEST_FRQ,ZIPF_ETA,N_ITER,N_REQUESTS,CACHE_SIZE,LIBRARY_SIZE,SEED'


    def __str__(self):
        headers, data = self.csv()
        return f'{headers}\n{data}'

    def csv(self):
        d = self.data()
        s = ''
        stat = self.request_frq, self.zipf_eta, self.n_iter, self.n_requests, self.cache_size, self.library_size, self.seed,
        for tpl in d:
            s += ','.join(map(str,tpl+stat)) + f'\n'
        s.rstrip("\n")

        self.csv_str = s+'\n'

        return self.headers, self.csv_str

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

        self.table_str=tabulate(data,
                                headers = headers,
                                tablefmt=tblfmt)

        return self.table_str


    def data(self, col=None):
        d = [(a, *[result for pm, result in pms.items()]) for a, pms in self.items()]
        if col is None:
            return d
        else:
            return [(t[0],t[col]) for t in d]
