class Gym:

    __REPR_ORDER = ('Subscription', 'Customer', 'Trainer', 'Equipment', 'ExercisePlan')

    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

        self.__ref_to = {
            'Customer': self.customers,
            'Trainer': self.trainers,
            'Equipment': self.equipment,
            'ExercisePlan': self.plans,
            'Subscription': self.subscriptions
        }

        self.add_customer = self.__add_object
        self.add_trainer = self.__add_object
        self.add_equipment = self.__add_object
        self.add_plan = self.__add_object
        self.add_subscription = self.__add_object

    def __add_object(self, obj) -> None:
        obj_list = self.__ref_to.get(obj.__class__.__name__)
        if not any(obj.id == el.id for el in obj_list):
            obj_list.append(obj)

    def subscription_info(self, subscription_id: int):
        retval = ''
        for obj_type in Gym.__REPR_ORDER:
            for obj in self.__ref_to.get(obj_type, []):
                if obj.id == subscription_id:
                    retval += repr(obj) + '\n'
        return retval.rstrip()
