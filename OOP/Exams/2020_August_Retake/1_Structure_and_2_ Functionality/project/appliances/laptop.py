from project.appliances.appliance import Appliance


class Laptop(Appliance):

    _COST = 1

    def __init__(self):
        super().__init__(self.__class__._COST)
