from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:

    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        return self.__class__.add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        return self.__class__.add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        return self.__class__.add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        return self.__class__.add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        return self.__class__.add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        retval = ''
        for el in ('subscriptions', 'customers', 'trainers', 'equipment', 'plans'):
            for obj in self.__dict__.get(el, []):
                if obj.id == subscription_id:
                    retval += repr(obj) + '\n'
        return retval.rstrip()

    @staticmethod
    def add_object(obj, obj_list) -> None:
        if not any(obj.id == el.id for el in obj_list):
            obj_list.append(obj)
