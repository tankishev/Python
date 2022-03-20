from project.drink.tea import Tea
from project.drink.water import Water
from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.baked_food.baked_food import BakedFood
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class ObjectFactory:

    @staticmethod
    def food(food_type: str, name: str, price: float):
        if food_type == "Bread":
            return Bread(name, price)
        elif food_type == "Cake":
            return Cake(name, price)

    @staticmethod
    def drink(drink_type: str, name: str, portion: float, brand: str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def table(table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)


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
    def name(self, value: str):
        if value == '' or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ("Bread", "Cake"):
            if any(food.name == name for food in self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")
            new_food = ObjectFactory.food(food_type, name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ("Tea", "Water"):
            if any(drink.name == name for drink in self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")
            new_drink = ObjectFactory.drink(drink_type, name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ("InsideTable", "OutsideTable"):
            if any(table.table_number == table_number for table in self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")
            new_table = ObjectFactory.table(table_type, table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        found_table = self.__get_free_table(number_of_people)
        if found_table:
            found_table.reserve(number_of_people)
            return f"Table {found_table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        found_table = self.__get_table_by_number(table_number)
        if found_table:
            skipped_items = []
            for food_name in food_names:
                try:
                    food = next(food for food in self.food_menu if food.name == food_name)
                    found_table.order_food(food)
                except StopIteration:
                    skipped_items.append(food_name)
                finally:
                    retval = found_table.food_order
                    if skipped_items:
                        retval += f'{self.name} does not have in the menu:\n'
                        retval += '\n'.join(skipped_items)
                    return retval.rstrip()
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drink_names: str):
        found_table = self.__get_table_by_number(table_number)
        if found_table:
            skipped_items = []
            for drink_name in drink_names:
                try:
                    drink = next(drink for drink in self.drinks_menu if drink.name == drink_name)
                    found_table.order_drink(drink)
                except StopIteration:
                    skipped_items.append(drink_name)
                finally:
                    retval = found_table.drink_order
                    if skipped_items:
                        retval += f'{self.name} does not have in the menu:\n'
                        retval += '\n'.join(skipped_items)
                    return retval.rstrip()
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

    def __get_table_by_number(self, table_number: int) -> Table:
        try:
            found_table = next(table for table in self.tables_repository if table.table_number == table_number)
            return found_table
        except StopIteration:
            pass

    def __get_free_table(self, number_of_people: int) -> Table:
        for table in self.tables_repository:
            if table.capacity <= number_of_people and not table.is_reserved:
                return table
