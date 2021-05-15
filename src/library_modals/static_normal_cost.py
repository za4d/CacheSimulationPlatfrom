import numpy as np
from library_modals import CostModel

class StaticNormalCost(CostModel):
    name='cost_normal'
    def __init__(self, length, mean=100, std=10):
        super().__init__({file: abs(np.random.normal(mean, std)) for file in range(length)})

    @property
    def params(self):
        return ['mean','std']
