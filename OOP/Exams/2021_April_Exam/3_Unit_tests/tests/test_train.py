import unittest
from project.train.train import Train


class TrainTests(unittest.TestCase):

    def setUp(self) -> None:
        self._TRAIN_FULL = "Train is full"
        self._PASSENGER_EXISTS = "Passenger {} Exists"
        self._PASSENGER_NOT_FOUND = "Passenger Not Found"
        self._PASSENGER_ADD = "Added passenger {}"
        self._PASSENGER_REMOVED = "Removed {}"
        self.t = Train('Fast', 10)

    def test_init(self):
        self.assertEqual(self.t.name, 'Fast')
        self.assertEqual(self.t.capacity, 10)
        self.assertListEqual(self.t.passengers, [])
        self.assertTrue(hasattr(self.t, 'add'))
        self.assertTrue(hasattr(self.t, 'remove'))

    def test_add_success(self):
        retval = self.t.add('Lyubo')
        self.assertEqual(self._PASSENGER_ADD.format('Lyubo'), retval)
        self.assertTrue('Lyubo' in self.t.passengers)
        self.assertEqual(len(self.t.passengers), 1)

    def test_add_no_capacity(self):
        self.t.capacity = 1
        self.t.add('Bobi')
        with self.assertRaises(ValueError) as context:
            self.t.add('Lyubo')
        self.assertEqual(self._TRAIN_FULL, str(context.exception))
        self.assertListEqual(self.t.passengers, ['Bobi'])

    def test_add_existing_passenger(self):
        self.t.add('Bobi')
        with self.assertRaises(ValueError) as context:
            self.t.add('Bobi')
        self.assertEqual(self._PASSENGER_EXISTS.format('Bobi'), str(context.exception))

    def test_remove_success(self):
        self.t.add('Bobi')
        self.t.add('Lyubo')
        retval = self.t.remove('Bobi')
        self.assertEqual(self._PASSENGER_REMOVED.format('Bobi'), retval)
        self.assertListEqual(self.t.passengers, ['Lyubo'])

    def test_remove_non_existing_passenger(self):
        with self.assertRaises(ValueError) as contex:
            self.t.remove('Lyubo')
        self.assertEqual(self._PASSENGER_NOT_FOUND.format('Lyubo'), str(contex.exception))


if __name__ == '__main__':
    unittest.main()
