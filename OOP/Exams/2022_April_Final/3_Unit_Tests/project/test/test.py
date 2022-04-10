from project.movie import Movie
import unittest


class MovieTests(unittest.TestCase):

    def setUp(self) -> None:
        name = "The Matrix"
        year = 1999
        rating = 8.7
        self.movie = Movie(name, year, rating)

    def test_name_setter_valid(self):
        new_name = "The Matrix Reloaded"
        self.movie.name = new_name
        self.assertEqual(new_name, self.movie.name)

    def test_name_setter_invalid(self):
        new_name = ""
        old_name = self.movie.name
        expected = "Name cannot be an empty string!"
        with self.assertRaises(ValueError) as err:
            self.movie.name = new_name
        self.assertEqual(expected, str(err.exception))
        self.assertEqual(old_name, self.movie.name)

    def test_year_setter_valid(self):
        new_year = 2001
        self.movie.year = new_year
        self.assertEqual(new_year, self.movie.year)

    def test_year_setter_invalid(self):
        new_year = 1886
        old_year = self.movie.year
        expected = "Year is not valid!"
        with self.assertRaises(ValueError) as err:
            self.movie.year = new_year
        self.assertEqual(expected, str(err.exception))
        self.assertEqual(old_year, self.movie.year)

    def test_add_new_actor(self):
        name = "Keanu Reeves"
        retval = self.movie.add_actor(name)
        self.assertIn(name, self.movie.actors)
        self.assertIsNone(retval)

    def test_add_exiting_actor(self):
        name = "Keanu Reeves"
        self.movie.add_actor(name)
        retval = self.movie.add_actor(name)
        expected = f"{name} is already added in the list of actors!"
        self.assertIn(name, self.movie.actors)
        self.assertEqual(retval, expected)

    def test_gt_better(self):
        other_name = "The Matrix Reloaded"
        other_movie = Movie(other_name, 2003, 7.2)
        expected = f'"{self.movie.name}" is better than "{other_name}"'
        retval = (self.movie > other_movie)
        self.assertEqual(expected, retval)

    def test_gt_worse(self):
        other_name = "The Matrix Reloaded"
        other_movie = Movie(other_name, 2003, 9.2)
        expected = f'"{other_name}" is better than "{self.movie.name}"'
        retval = (self.movie > other_movie)
        self.assertEqual(expected, retval)

    def test_repr(self):
        actor1 = "Keanu Reeves"
        actor2 = "Laurence Fishburne"
        self.movie.add_actor(actor1)
        self.movie.add_actor(actor2)
        expected = f"Name: The Matrix\n" \
                   f"Year of Release: 1999\n" \
                   f"Rating: 8.70\n" \
                   f"Cast: Keanu Reeves, Laurence Fishburne"
        actual = repr(self.movie)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
