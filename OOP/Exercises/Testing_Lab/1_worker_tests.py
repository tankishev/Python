import unittest


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'Me'
        self.salary = 1000
        self.energy = 50

        self.w = Worker(self.name, self.salary, self.energy)

    def test_init(self):
        self.assertEqual(self.w.name, self.name)
        self.assertEqual(self.w.salary, self.salary)
        self.assertEqual(self.w.energy, self.energy)

    def test_energy_incremented_after_rest(self):
        start_energy = self.w.energy
        self.w.rest()
        self.assertGreater(self.w.energy, start_energy)

    def test_error_if_working_with_zero_or_negative_energy(self):
        self.w.energy = 0
        with self.assertRaises(Exception) as contex:
            self.w.work()
        self.assertTrue('Not enough energy' in str(contex.exception))
        self.w.energy = -1
        with self.assertRaises(Exception) as contex:
            self.w.work()
        self.assertTrue('Not enough energy' in str(contex.exception))

    def test_money_increased_with_salary_after_working(self):
        expected = self.w.salary + self.w.money
        self.w.work()
        self.assertEqual(self.w.money, expected)

    def test_worker_energy_decreased_after_work(self):
        starting_energy = self.w.energy
        self.w.work()
        self.assertLess(self.w.energy, starting_energy)

    def test_get_info_method(self):
        expected = f'{self.w.name} has saved {self.w.money} money.'
        self.assertEqual(self.w.get_info(), expected)


if __name__ == '__main__':
    unittest.main()
