# Create a class called Book. It should have an __init__() method that should receive:
# •	name: string
# •	author: string
# •	pages: int


class Book:

    def __init__(self, name: str, author: str, pages: int) -> None:
        self.name = name
        self.author = author
        self.pages = pages

