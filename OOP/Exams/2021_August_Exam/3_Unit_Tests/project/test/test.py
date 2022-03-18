from project.pet_shop import PetShop
import unittest


class PetShopTests(unittest.TestCase):

    def setUp(self) -> None:
        self.p = PetShop("Friends")
        self.p.add_food("cat food", 190)
        self.p.add_pet("Flerken")
        self.p.feed_pet("cat food", "Flerken")

    def test_init(self):
        self.assertEqual(self.p.name, "Friends")
        self.assertListEqual(self.p.pets, ["Flerken"])
        self.assertDictEqual(self.p.food, {"cat food": 90})

    def test_add_food_successful(self):
        retval = self.p.add_food("live mice", 200.30)
        self.assertEqual(retval, "Successfully added 200.30 grams of live mice.")

    def test_add_pet_successful(self):
        retval = self.p.add_pet("rhino")
        self.assertEqual(retval, 'Successfully added rhino.')
        self.assertListEqual(self.p.pets, ["Flerken", "rhino"])

    def test_add_pet_fail_repeat_pet(self):
        with self.assertRaises(Exception) as context:
            self.p.add_pet("Flerken")
        self.assertEqual(str(context.exception), "Cannot add a pet with the same name")

    def test_add_food_quantity_below_zero(self):
        with self.assertRaises(ValueError) as contex:
            self.p.add_food("zero", 0)
        self.assertEqual(str(contex.exception), "Quantity cannot be equal to or less than 0")
        with self.assertRaises(ValueError) as contex:
            self.p.add_food("minus", -1000)
        self.assertEqual(str(contex.exception), "Quantity cannot be equal to or less than 0")

    def test_feed_pet_successful(self):
        retval_adding_food = self.p.feed_pet("cat food", "Flerken")
        retval = self.p.feed_pet("cat food", "Flerken")
        self.assertEqual(retval_adding_food, "Adding food...")
        self.assertEqual(retval, "Flerken was successfully fed")
        self.assertEqual(self.p.food.get("cat food", None), 990)

    def test_feed_pet_no_such_food(self):
        retval = self.p.feed_pet("lemons", "Flerken")
        self.assertEqual(retval, 'You do not have lemons')

    def test_feed_pet_no_such_pet(self):
        with self.assertRaises(Exception) as context:
            self.p.feed_pet("cat food", "elephant")
        self.assertEqual(str(context.exception), 'Please insert a valid pet name')

    def test_repr(self):
        retval = f'Shop {self.p.name}:\n' \
                 f'Pets: {", ".join(self.p.pets)}'
        self.assertEqual(repr(self.p), retval)


if __name__ == '__main__':
    unittest.main()

