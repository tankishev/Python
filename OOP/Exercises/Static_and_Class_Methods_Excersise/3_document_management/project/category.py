class Category:

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def edit(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
