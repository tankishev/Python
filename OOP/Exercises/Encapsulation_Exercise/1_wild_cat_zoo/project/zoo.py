from .animal import Animal
from .worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal: Animal, price) -> str:
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        payroll_expense = self._payroll_cost()
        if self.__budget >= payroll_expense:
            self.__budget -= payroll_expense
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animal_care_cost = self._animal_cost()
        if self.__budget >= animal_care_cost:
            self.__budget -= animal_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        if amount > 0:
            self.__budget += amount

    def animals_status(self) -> str:
        return self._get_statuses('animals', ('Lion', 'Tiger', 'Cheetah'))

    def workers_status(self):
        return self._get_statuses('workers', ('Keeper', 'Caretaker', 'Vet'))

    #  helper functions
    def _payroll_cost(self) -> int:
        return sum([worker.salary for worker in self.workers])

    def _animal_cost(self) -> int:
        return sum([animal.money_for_care for animal in self.animals])

    def _get_statuses(self, obj_type: str, obj_names: tuple) -> str:
        obj_list = getattr(self, obj_type)
        obj_count = {obj: list() for obj in obj_names}
        for obj in obj_list:
            obj_count[obj.__class__.__name__].append(repr(obj))

        retval = f'You have {len(obj_list)} {obj_type}'
        for k, v in obj_count.items():
            retval += f'\n----- {len(v)} {k}s:'
            if v:
                retval += '\n' + '\n'.join(v)

        return retval
