from project.bakery import Bakery
import unittest


class BakeryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.b = Bakery("BratyaPekari")
        self.b.add_table("InsideTable", 2, 5)
        self.b.add_table("OutsideTable", 52, 8)
        self.b.add_food("Bread", "Italian Bread", 1.55)
        self.b.add_food("Cake", "Cheesecake", 6.22)
        self.b.add_drink("Water", "Sparkling water", 500, "SanPellegrino")
        self.b.add_drink("Tea", "Lemon Ice Tea", 250, "Lipton")

    def test_add_food_throws_error_for_exiting_name(self):
        food_type_one = "Cake"
        food_type_two = "Bread"
        food_name = "Italian Bread"
        food_price = 5.55
        with self.assertRaises(Exception) as context:
            self.b.add_food(food_type_one, food_name, food_price)
        self.assertEqual(str(context.exception), f"{food_type_one} {food_name} is already in the menu!")
        with self.assertRaises(Exception) as context:
            self.b.add_food(food_type_two, food_name, food_price)
        self.assertEqual(str(context.exception), f"{food_type_two} {food_name} is already in the menu!")

    def test_add_food_returns_none_for_non_existent_type(self):
        food_type = "WrongType"
        food_name = "Red Velvet"
        food_price = 6.66

        actual = self.b.add_food(food_type, food_name, food_price)
        self.assertIsNone(actual)

    def test_add_food_returns_proper_message(self):
        food_type = "Cake"
        food_name = "Red Velvet"
        food_price = 6.66

        actual = self.b.add_food(food_type, food_name, food_price)
        expected = f"Added {food_name} ({food_type}) to the food menu"
        self.assertEqual(actual, expected)

    def test_add_drink_throws_error_for_exiting_name(self):
        drink_type_one = "Water"
        drink_type_two = "Tea"
        drink_name = "Lemon Ice Tea"
        drink_brand = "Does Not Matter"
        drink_size = 125
        with self.assertRaises(Exception) as context:
            self.b.add_drink(drink_type_one, drink_name, drink_size, drink_brand)
        self.assertEqual(str(context.exception), f"{drink_type_one} {drink_name} is already in the menu!")
        with self.assertRaises(Exception) as context:
            self.b.add_drink(drink_type_two, drink_name, drink_size, drink_brand)
        self.assertEqual(str(context.exception), f"{drink_type_two} {drink_name} is already in the menu!")

    def test_add_drink_returns_none_for_non_existent_type(self):
        drink_type= "WrongType"
        drink_name = "Beer"
        drink_brand = "Heiniken"
        drink_size = 500

        actual = self.b.add_drink(drink_type, drink_name, drink_size, drink_brand)
        self.assertIsNone(actual)

    def test_add_drink_returns_proper_message(self):
        drink_type= "Tea"
        drink_name = "Peach Ice Tea"
        drink_brand = "Lipton"
        drink_size = 500

        actual = self.b.add_drink(drink_type, drink_name, drink_size, drink_brand)
        expected = f"Added {drink_name} ({drink_brand}) to the drink menu"
        self.assertEqual(actual, expected)

    def test_add_table_throws_error_for_exiting_number(self):
        table_type = "InsideTable"
        table_number = 2
        table_capacity = 10

        with self.assertRaises(Exception) as context:
            self.b.add_table(table_type, table_number, table_capacity)
        self.assertEqual(str(context.exception), f"Table {table_number} is already in the bakery!")

    def test_add_table_returns_none_for_non_existent_type(self):
        table_type = "PoolSideTable"
        table_number = 200
        table_capacity = 10

        actual = self.b.add_table(table_type, table_number, table_capacity)
        self.assertIsNone(actual)

    def test_add_table_returns_proper_message(self):
        table_type = "InsideTable"
        table_number = 5
        table_capacity = 10

        actual = self.b.add_table(table_type, table_number, table_capacity)
        expected = f"Added table number {table_number} in the bakery"
        self.assertEqual(actual, expected)

    def test_reserve_returns_reserved_if_table_is_available(self):
        table_number = 52
        number_of_people = 7
        actual = self.b.reserve_table(number_of_people)
        expected = f"Table {table_number} has been reserved for {number_of_people} people"
        self.assertEqual(actual, expected)

    def test_reserve_returns_unavailable_if_no_table_with_such_capacity(self):
        number_of_people = 14
        actual = self.b.reserve_table(number_of_people)
        expected = f"No available table for {number_of_people} people"
        self.assertEqual(actual, expected)

    def test_reserve_returns_unavailable_if_no_available_table(self):
        number_of_people = 7
        self.b.reserve_table(number_of_people)
        actual = self.b.reserve_table(number_of_people)
        expected = f"No available table for {number_of_people} people"
        self.assertEqual(actual, expected)

    def test_get_free_table_returns_empty_if_no_table_available(self):
        self.b.reserve_table(2)
        self.b.reserve_table(2)
        actual = self.b.get_free_tables_info()
        self.assertEqual(actual, '')

    def test_order_food_cannot_find_table(self):
        table_number = 3
        actual = self.b.order_food(table_number, "does not really matter")
        expected = f"Could not find table {table_number}"
        self.assertEqual(actual, expected)

    def test_order_food_returns_proper_message(self):
        table_number = 2
        food_order = ("Cake", "Cheesecake", "Italian Bread", "Bread")
        actual = self.b.order_food(table_number, *food_order)
        expected = "Table 2 ordered:" \
                   "\n - Cheesecake: 245.00g - 6.22lv" \
                   "\n - Italian Bread: 200.00g - 1.55lv" \
                   "\nBratyaPekari does not have in the menu:" \
                   "\nCake" \
                   "\nBread"
        self.assertEqual(actual, expected)

    def test_order_drink_cannot_find_table(self):
        table_number = 3
        actual = self.b.order_drink(table_number, "does not really matter")
        expected = f"Could not find table {table_number}"
        self.assertEqual(actual, expected)

    def test_order_drink_returns_proper_message(self):
        table_number = 2
        drink_order = ("Beer", "Lemon Ice Tea", "Wine", "Sparkling water")
        actual = self.b.order_drink(table_number, *drink_order)
        expected = "Table 2 ordered:" \
                   "\n - Lemon Ice Tea Lipton - 250.00ml - 2.50lv" \
                   "\n - Sparkling water SanPellegrino - 500.00ml - 1.50lv" \
                   "\nBratyaPekari does not have in the menu:" \
                   "\nBeer" \
                   "\nWine"
        self.assertEqual(actual, expected)

    def test_leave_table_returns_proper_bill(self):
        table_number = 52
        self.b.reserve_table(7)
        food_order = ("Cake", "Cheesecake", "Italian Bread", "Bread")
        self.b.order_food(table_number, *food_order)
        drink_order = ("Beer", "Lemon Ice Tea", "Wine", "Sparkling water")
        self.b.order_drink(table_number, *drink_order)

        actual = self.b.leave_table(table_number)
        expected = "Table: 52" \
                   "\nBill: 11.77"
        self.assertEqual(actual, expected)

    def test_leave_table_clears_table(self):
        table_number = 52
        self.b.reserve_table(7)
        food_order = ("Cake", "Cheesecake", "Italian Bread", "Bread")
        self.b.order_food(table_number, *food_order)
        self.b.leave_table(table_number)

        table_obj = [table for table in self.b.tables_repository if table.table_number == 52][0]
        self.assertFalse(table_obj.is_reserved)
        self.assertEqual(len(table_obj.food_orders), 0)
        self.assertEqual(len(table_obj.drink_orders), 0)

    def test_leave_table_increases_bill_correctly(self):
        table_number = 52
        self.b.reserve_table(7)
        food_order = ("Cake", "Cheesecake", "Italian Bread", "Bread")
        self.b.order_food(table_number, *food_order)

        starting_income = 12
        self.b.total_income = starting_income
        self.b.leave_table(table_number)

        actual = self.b.total_income
        expected = 19.77
        self.assertEqual(actual, expected)
        self.assertEqual(self.b.get_total_income(), f"Total income: {expected}lv")

    def test_get_free_table_returns_proper_message(self):
        expected = "Table: 2" \
                   "\nType: InsideTable" \
                   "\nCapacity: 5" \
                   "\nTable: 52" \
                   "\nType: OutsideTable" \
                   "\nCapacity: 8"
        actual = self.b.get_free_tables_info()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

