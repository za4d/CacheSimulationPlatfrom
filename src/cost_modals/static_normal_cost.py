import numpy as np
from cost_modals import StaticCost

class StaticNormalCost(StaticCost):

    def __init__(self, length, mean=100, std=10):
        super().__init__({file: abs(np.random.normal(mean, std)) for file in range(length)})

    @property
    def params(self):
        return ['mean','std']
