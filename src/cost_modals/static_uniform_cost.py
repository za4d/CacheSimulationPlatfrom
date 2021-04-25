import numpy as np
from src.cost_modals._cost_modal import StaticCost

class StaticUniformCost(StaticCost):

    def __init__(self, length, cost=1):
        super().__init__({file: cost for file in range(length)})

