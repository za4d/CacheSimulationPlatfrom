from _communication_modal import CommunicationModal

class StaticCost(CommunicationModal):

    def __init__(self, dict):
        self.cost_func = dict

    def cost(self, file, src=None, dst=None):
        return self.cost_func[file]