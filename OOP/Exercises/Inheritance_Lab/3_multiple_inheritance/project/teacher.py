from .person import Person
from .employee import Employee


class Teacher(Person, Employee):

    def __init__(self) -> None:
        pass

    def teach(self):
        return 'teaching...'