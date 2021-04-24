from abc import ABC, abstractmethod


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

######################################


class Car(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def run(self,n):
        x = np.ran

    def set(self, o):
        self.other = o


