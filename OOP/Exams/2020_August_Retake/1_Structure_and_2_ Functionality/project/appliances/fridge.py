from project.appliances.appliance import Appliance


class Fridge(Appliance):

    _COST = 1.2

    def __init__(self):
        super().__init__(self.__class__._COST)
