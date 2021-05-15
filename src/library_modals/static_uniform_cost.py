import numpy as np
from library_modals import CostModel

class StaticUniformCost(CostModel):
    name='cost_uniform'
    def __init__(self, length, cost=1):
        super().__init__({file: cost for file in range(length)})

    @property
    def params(self):
        return ['cost']
