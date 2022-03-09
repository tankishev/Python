from .customer import Customer
from .dvd import DVD


class MovieWorld:

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        return customer.rent_dvd(dvd)

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return customer.return_dvd(dvd)
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        retval = ''
        if self.customers:
            retval += '\n'.join([repr(customer) for customer in self.customers])
        if self.dvds:
            if self.customers:
                retval += '\n'
            retval += '\n'.join([repr(dvd) for dvd in self.dvds])
        return retval

    def __get_customer(self, customer_id: int) -> Customer:
        return next(customer for customer in self.customers if customer.id == customer_id)

    def __get_dvd(self, dvd_id: int) -> DVD:
        return next(dvd for dvd in self.dvds if dvd.id == dvd_id)
