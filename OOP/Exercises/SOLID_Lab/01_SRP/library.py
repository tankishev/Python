from .books import Book


class Library:

    def __init__(self) -> None:
        self.books = []

    def find_book(self, book: Book) -> Book:
        try:
            found_book = next(b for b in self.books if b.title == book.title)
            return found_book
        except StopIteration:
            pass
