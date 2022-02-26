from .person import Person
from .employee import Employee


class Teacher(Person, Employee):

    def __init__(self) -> None:
        super().__init__()

    def teach(self):
        return 'teaching...'
