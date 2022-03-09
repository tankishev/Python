from .helper_class import AIBC


class Trainer(AIBC):

    def __init__(self, name: str) -> str:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
