from .helper_class import AIBC


class Customer(AIBC):

    def __init__(self, name: str, address: str, email: str) -> None:
        super().__init__()
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
