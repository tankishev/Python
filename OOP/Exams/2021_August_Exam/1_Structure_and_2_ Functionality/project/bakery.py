from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class ObjectFactory:

    @staticmethod
    def food(food_type: str, name: str, price: float):
        if food_type in ("Bread", "Cake"):
            return eval(f'{food_type}("{name}", {price})')

    @staticmethod
    def drink(drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ("Tea", "Water"):
            return eval(f'{drink_type}("{name}", {portion}, "{brand}")')

    @staticmethod
    def table(table_type: str, table_number: int, capacity: int):
        if table_type in ("InsideTable", "OutsideTable"):
            return eval(f'{table_type}({table_number}, {capacity})')


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        new_food = ObjectFactory.food(food_type, name, price)
        if new_food:
            if any(food.name == name for food in self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        new_drink = ObjectFactory.drink(drink_type, name, portion, brand)
        if new_drink:
            if any(drink.name == name for drink in self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        new_table = ObjectFactory.table(table_type, table_number, capacity)
        if new_table:
            if any(table.table_number == table_type for table in self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            reserve_table = next(table for table in self.tables_repository
                                 if table.capacity >= number_of_people and not table.is_reserved)
            reserve_table.reserve(number_of_people)
            return f"Table {reserve_table.table_number} has been reserved for {number_of_people} people"
        except StopIteration:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        found_table = self.__get_table_by_number(table_number)
        if found_table:
            for food in food_names:
                if food in self.food_menu:
                    found_table.order_food(food)
            return self.__read_order(table_number, found_table.food_orders, *food_names)
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drink_names: str):
        found_table = self.__get_table_by_number(table_number)
        if found_table:
            for drink in drink_names:
                if drink in self.drinks_menu:
                    found_table.order_drink(drink)
            return self.__read_order(table_number, found_table.drink_orders, *drink_names)
        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        found_table = self.__get_table_by_number(table_number)
        if found_table:
            retval = f'"Table: {table_number}' \
                     f'\nBill: {found_table.get_bill():.2f}'
            found_table.clear()
            return retval

    def get_free_tables_info(self):
        return '\n'.join([table.free_table_info() for table in self.tables_repository if not table.is_reserved])

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

    def __get_table_by_number(self, table_number: int):
        try:
            found_table = next(table for table in self.tables_repository if table.table_number == table_number)
            return found_table
        except StopIteration:
            pass

    def __read_order(self, table_number, order_list, *items):
        retval = f"Table {table_number} ordered:"
        if len(order_list) > 0:
            retval += '\n' + '\n'.join([repr(el) for el in order_list])

        retval += f'{self.name} does not have in the menu:'
        if len(order_list) < len(items):
            retval += '\n' + '\n'.join([el.name for el in items if el not in order_list])

        return retval
