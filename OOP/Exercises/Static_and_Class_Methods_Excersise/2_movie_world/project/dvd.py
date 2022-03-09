from datetime import datetime


class DVD:

    def __init__(self, name: str, id_: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.__is_rented = False

    @classmethod
    def from_date(cls, id_: int, name: str, date: str, age_restriction: int):
        dvd_date = datetime.strptime(date, '%d.%m.%Y')
        return cls(name, id_, int(dvd_date.strftime("%Y")), dvd_date.strftime("%B"), age_restriction)

    @property
    def is_rented(self):
        return self.__is_rented

    def rent_dvd(self) -> None:
        self.__is_rented = True

    def return_dvd(self) -> None:
        self.__is_rented = False

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {('not rented','rented')[self.__is_rented]}"
