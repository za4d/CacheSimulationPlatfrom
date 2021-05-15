import numpy as np
from library_modals import CostModel

class StaticRandomCost(CostModel):
    name='cost_random'
    def __init__(self, length, high=1000):
        super().__init__({file: np.random.randint(high) for file in range(length)})

    @property
    def params(self):
        return ['high']