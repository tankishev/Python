from project.appliances.appliance import Appliance


class TV(Appliance):

    _COST = 1.5

    def __init__(self):
        super().__init__(self.__class__._COST)
