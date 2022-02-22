# Create a class called Shop. Upon initialization it should receive a name (string) and items (list).
# Create a method called get_items_count() which should return the number of items in the store.


class Shop:

    def __init__(self, name: str, items: list) -> None:
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        return len(self.items)
