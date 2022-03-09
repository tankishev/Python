from .dvd import DVD


class Customer:

    def __init__(self, name: str, age: int, id_: int) -> None:
        self.name = name
        self.age = age
        self.id = id_
        self.rented_dvds = []

    def rent_dvd(self, dvd: DVD) -> str:
        self.rented_dvds.append(dvd)
        dvd.rent_dvd()
        return f"{self.name} has successfully rented {dvd.name}"

    def return_dvd(self, dvd: DVD) -> str:
        self.rented_dvds.remove(dvd)
        dvd.return_dvd()
        return f"{self.name} has successfully returned {dvd.name}"

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join([dvd.name for dvd in self.rented_dvds])})"
