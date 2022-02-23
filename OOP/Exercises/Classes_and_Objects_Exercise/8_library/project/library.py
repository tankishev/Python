# In the library.py create a class Library. Upon initialization, it will not receive anything,
# but it should have the following instance attributes:
# -	user_records - an empty list that will store the users (users objects) of the library
# -	books_available - an empty dictionary {author: [book_name, ]}
# -	rented_books - an empty dictionary {usernames: {book names: days to return}}.
# You should also create 2 additional instance methods:
# -	get_book(author: str, book_name: str, days_to_return: int, user: User):
# -->	If the book is available in the library adds it to the books list for this user,
#       updates the library records (rented_books and available_books dicts), and returns the following message:
#       "{book_name} successfully rented for the next {days_to_return} days!"
# -->	If it is already rented, returns the following message "The book "{book_name}" is already rented
# and will be available in {days_to_return provided by the user rented the book} days!"

# -	return_book(author:str, book_name:str, user: User):
# -->	If the book is in the user's books list, returns it in the library (update books_available
#       and rented_books class attributes) and removes it from the books list for this user
# -->	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"


from .user import User


class Library:

    def __init__(self) -> None:
        self.user_records = []
        self.books_available = {}   # {author: [book_name, ]}
        self.rented_books = {}      # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if book_name in self.books_available.get(author, []):
            user.books.append(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})

            self.books_available[author].remove(book_name)
            # if len(self.books_available[author]) < 1:
            #     self.books_available.pop(author)

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        else:
            search_results = []
            for username in self.rented_books.keys():
                if book_name in self.rented_books[username].keys():
                    search_results.append((username, self.rented_books[username].get(book_name)))
            if search_results:
                # search_results.sort()
                return f'The book "{book_name}" is already rented and will be ' \
                       f'available in {search_results[0][1]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)

            if book_name in self.rented_books[user.username].keys():
                self.rented_books[user.username].pop(book_name)
            if len(self.rented_books[user.username]) < 1:
                self.rented_books.pop(user.username)

            if author not in self.books_available.keys():
                self.books_available[author] = []
            self.books_available[author].append(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
