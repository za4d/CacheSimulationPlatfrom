import numpy as np
from cost_modals import StaticCost

class StaticRandomCost(StaticCost):
    name='static_random_cost'
    def __init__(self, length, high=1000):
        super().__init__({file: np.random.randint(high) for file in range(length)})

    @property
    def params(self):
        return ['high']