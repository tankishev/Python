from .person import Person


class Child(Person):

    def __init__(self, *args):
        super().__init__(*args)
