from project.library import Library
import unittest


class LibraryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library('MyLib')

    def test_init(self):
        name = 'MyLib'
        self.assertEqual(name, self.library.name)
        self.assertDictEqual({}, self.library.readers)
        self.assertDictEqual({}, self.library.books_by_authors)

    def test_name_setter(self):
        name = 'ChangeName'
        self.library.name = name
        self.assertTrue(hasattr(self.library, '_Library__name'))
        self.assertEqual(getattr(self.library, '_Library__name'), name)
        self.assertEqual(self.library.name, name)

        err_message = "Name cannot be empty string!"
        with self.assertRaises(ValueError) as context:
            Library('')
        self.assertEqual(err_message, str(context.exception))

    def test_add_book(self):
        author = 'Rowling'
        title = 'Harry Potter'
        title_2 = 'James Potter'

        retval = self.library.add_book(author, title)
        self.library.add_book(author, title)
        expected = {author: [title]}
        self.assertDictEqual(expected, self.library.books_by_authors)
        self.assertIsNone(retval)

        self.library.add_book(author, title_2)
        expected = {author: [title, title_2]}
        self.assertDictEqual(expected, self.library.books_by_authors)

    def test_add_reader_successful(self):
        name = 'Bobi'

        retval = self.library.add_reader(name)
        expected = {name: []}
        self.assertDictEqual(expected, self.library.readers)
        self.assertIsNone(retval)

    def test_add_reader_fail(self):
        name = 'Bobi'
        err_message = f"{name} is already registered in the {self.library.name} library."

        self.library.add_reader(name)
        actual = self.library.add_reader(name)
        self.assertEqual(err_message, actual)

    def test_rent_successful(self):
        reader_name = 'Bobi'
        book_author = 'Rowling'
        book_1 = 'Harry Potter'
        book_2 = 'James Potter'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, book_1)
        self.library.add_book(book_author, book_2)

        retval = self.library.rent_book(reader_name, book_author, book_1)
        self.assertIsNone(retval)

        expected_reader_dict = {reader_name: [{book_author: book_1}]}
        self.assertDictEqual(expected_reader_dict, self.library.readers)

        expected_books_dict = {book_author: [book_2]}
        self.assertDictEqual(expected_books_dict, self.library.books_by_authors)

    def test_rent_no_such_reader(self):
        reader_name = 'Bobi'
        book_author = 'Rowling'
        book_title = 'Harry Potter'

        expected = f"{reader_name} is not registered in the {self.library.name} Library."
        actual = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(expected, actual)

    def test_rent_no_such_author(self):
        reader_name = 'Bobi'
        book_author = 'Rowling'
        book_title = 'Harry Potter'

        self.library.add_reader(reader_name)
        expected = f"{self.library.name} Library does not have any {book_author}'s books."
        actual = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(expected, actual)

    def test_rent_no_such_book(self):
        reader_name = 'Bobi'
        book_author = 'Rowling'
        book_title = 'Harry Potter'
        wrong_title = 'James Potter'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, book_title)
        expected = f"""{self.library.name} Library does not have {book_author}'s "{wrong_title}"."""
        actual = self.library.rent_book(reader_name, book_author, wrong_title)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()