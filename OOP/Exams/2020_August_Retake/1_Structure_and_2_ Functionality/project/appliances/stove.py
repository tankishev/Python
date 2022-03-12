from project.appliances.appliance import Appliance


class Stove(Appliance):

    _COST = 0.7

    def __init__(self):
        super().__init__(self.__class__._COST)
