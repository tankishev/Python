from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatters(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class Formatter(Formatters):
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatters()):
        formatted_book = formatter.format(book)
        return formatted_book
