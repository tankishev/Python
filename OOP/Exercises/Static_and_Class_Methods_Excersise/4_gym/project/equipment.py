from .helper_class import AIBC


class Equipment(AIBC):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
