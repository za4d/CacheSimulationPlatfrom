
class VirtualCache(list):

    def __init__(self, init_state=None):
        super().__init__(init_state)

    def read(self, address):
        return super().__getitem__(address)

    def write(self, address, file):
        # self.checkIfDuplicates()
        super().__setitem__(address, file)

    def state(self):
        return self.copy()


    # def checkIfDuplicates(self):
    #     ''' Check if given list contains any duplicates '''
    #     print(self)
    #     if len(self) == len(set(self)):
    #         return False
    #     else:
    #         ''' Check if given list contains any duplicates '''
    #         s = set()
    #         dup = set()
    #         for elem in self:
    #             if elem in s:
    #                 dup.add(elem)
    #             else:
    #                 s.add(elem)
    #         return True