

class S(list):

    def __init__(self,l):
        super().__init__(l)

    def f(self,n):
        return self.other[:n]


    def set(self, o):
        self.other = o





class P(list):

    def __init__(self,l):
        super().__init__(l)

    def f(self,n):
        return self.other[n]

    def set(self, o):
        self.other = o



