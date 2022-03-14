import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class CarManagerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("Opel", "Astra", 10, 40)
        self.car.refuel(20)

    def test_init(self):
        self.assertEqual(self.car.make, 'Opel')
        self.assertEqual(self.car.model, 'Astra')
        self.assertEqual(self.car.fuel_capacity, 40)
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_getters_and_setters(self):
        self.car.make = 'GAZ'
        self.car.model = 'Volga'
        self.car.fuel_capacity = 30
        self.car.fuel_consumption = 15
        self.car.fuel_amount = 23
        self.assertEqual(self.car.make, 'GAZ')
        self.assertEqual(self.car.model, 'Volga')
        self.assertEqual(self.car.fuel_capacity, 30)
        self.assertEqual(self.car.fuel_consumption, 15)
        self.assertEqual(self.car.fuel_amount, 23)

    def test_all_attributes_name_mangled(self):
        self.assertTrue(hasattr(self.car, f'_Car__make'))
        self.assertTrue(hasattr(self.car, f'_Car__model'))
        self.assertTrue(hasattr(self.car, f'_Car__fuel_consumption'))
        self.assertTrue(hasattr(self.car, f'_Car__fuel_capacity'))

    def test_make_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''
        self.assertTrue("Make cannot be null or empty!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertTrue("Make cannot be null or empty!" in str(context.exception))

    def test_model_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertTrue("Model cannot be null or empty!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertTrue("Model cannot be null or empty!" in str(context.exception))

    def test_fuel_consumption_setter_cannot_set_negative_or_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -10
        self.assertTrue("Fuel consumption cannot be zero or negative!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertTrue("Fuel consumption cannot be zero or negative!" in str(context.exception))

    def test_fuel_capacity_setter_cannot_set_negative_or_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -10
        self.assertTrue("Fuel capacity cannot be zero or negative!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertTrue("Fuel capacity cannot be zero or negative!" in str(context.exception))

    def test_fuel_setter_cannot_set_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -10
        self.assertTrue("Fuel amount cannot be negative!" in str(context.exception))

    def test_fuel_correctly_top_up_on_refuel(self):
        self.car.refuel(self.car.fuel_capacity + 1)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)
        self.car.fuel_amount = 10
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 11)

    def test_exception_on_negative_refuel_amount(self):
        with self.assertRaises(Exception) as contex:
            self.car.refuel(-5)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(contex.exception))

    def test_exception_on_zero_refuel_amount(self):
        with self.assertRaises(Exception) as contex:
            self.car.refuel(0)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(contex.exception))

    def test_correct_remaining_fuel_after_drive(self):
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_exception_on_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as contex:
            self.car.drive(201)
        self.assertTrue("You don't have enough fuel to drive!" in str(contex.exception))


if __name__ == '__main__':
    unittest.main()
