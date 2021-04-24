from _cost_modal import CostModal

class StaticCost(CostModal):

    def __init__(self, dict):
        self.cost_func = dict

    def cost(self, file):
        return self.cost_func[file]
