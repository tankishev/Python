import unittest
from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):

    def test_init(self):
        factory = PaintFactory('my_factory', 20)
        self.assertEqual(factory.name, 'my_factory')
        self.assertEqual(factory.capacity, 20)
        self.assertListEqual(factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(factory.ingredients, factory.products)

    def test_adding_ingredient_successful(self):
        factory = PaintFactory('my_factory', 20)
        factory.add_ingredient('white', 10)
        self.assertTrue('white' in factory.ingredients)
        self.assertEqual(factory.ingredients.get('white', None), 10)

    def test_adding_wrong_ingredient_raises_error(self):
        factory = PaintFactory('my_factory', 20)
        with self.assertRaises(TypeError) as contex:
            factory.add_ingredient('black', 10)
        self.assertTrue("Ingredient of type black not allowed in PaintFactory" in str(contex.exception))

    def test_adding_ingredient_without_capacity_raises_error(self):
        factory = PaintFactory('my_factory', 20)
        with self.assertRaises(ValueError) as contex:
            factory.add_ingredient('white', 100)
        self.assertTrue("Not enough space in factory" in str(contex.exception))

    def test_remove_ingredient_successful(self):
        factory = PaintFactory('my_factory', 20)
        factory.add_ingredient('white', 10)
        factory.remove_ingredient('white', 9)
        self.assertEqual(factory.ingredients.get('white'), 1)

    def test_remove_ingredient_no_such_ingredient(self):
        factory = PaintFactory('my_factory', 20)
        with self.assertRaises(KeyError) as contex:
            factory.remove_ingredient('white', 20)
        self.assertTrue("No such ingredient in the factory" in str(contex.exception))

    def test_remove_ingredient_not_enough_ingredients(self):
        factory = PaintFactory('my_factory', 20)
        factory.add_ingredient('white', 10)
        with self.assertRaises(ValueError) as contex:
            factory.remove_ingredient('white', 20)
        self.assertTrue("Ingredients quantity cannot be less than zero" in str(contex.exception))

    def test_can_add_method(self):
        factory = PaintFactory('my_factory', 20)
        self.assertFalse(factory.can_add(21))
        self.assertTrue(factory.can_add(20))

    def test_repr(self):
        factory = PaintFactory('my_factory', 20)
        factory.add_ingredient('white', 10)
        expected = 'Factory name: my_factory with capacity 20.\n'
        expected += "white: 10\n"
        self.assertEqual(repr(factory), expected)


if __name__ == '__main__':
    unittest.main()
