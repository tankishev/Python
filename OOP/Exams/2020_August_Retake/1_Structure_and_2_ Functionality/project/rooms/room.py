class Room:

    _APPLIANCES = []
    _ROOM_COST = 0

    def __init__(self, family_name: str, budget: float, members_count: int) -> None:
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.expenses = 0

        self.room_cost = self.__class__._ROOM_COST

        self.children = []
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, amount: float):
        if amount < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = amount

    @property
    def monthly_cost(self):
        return self.__expenses + self.room_cost

    def calculate_expenses(self, *args) -> None:
        self.expenses = Room._calculate_expenses(*args)

    def pay_expenses(self) -> tuple:
        if self.budget >= self.monthly_cost:
            self.budget -= self.monthly_cost
            return True, f"{self.family_name} paid {self.monthly_cost:.2f}$ and have {self.budget:.2f}$ left."
        return False, f"{self.family_name} does not have enough budget and must leave the hotel."

    def status(self) -> str:
        retval = f'{self.family_name} with {self.members_count} members. ' \
                 f'Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$'
        if self.children:
            for i, child in enumerate(self.children):
                retval += f'\n--- Child {i+1} monthly cost: {child.get_monthly_expense():.2f}$'
        retval += f'\n--- Appliances monthly cost: {Room._calculate_expenses(self.appliances):.2f}$'
        return retval

    @staticmethod
    def _calculate_expenses(*args) -> float:
        return sum([el.get_monthly_expense() for arg in args for el in arg])
