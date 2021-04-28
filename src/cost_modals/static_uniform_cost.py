import numpy as np
from cost_modals import StaticCost

class StaticUniformCost(StaticCost):

    def __init__(self, length, cost=1):
        super().__init__({file: cost for file in range(length)})

    @property
    def params(self):
        return ['cost']
