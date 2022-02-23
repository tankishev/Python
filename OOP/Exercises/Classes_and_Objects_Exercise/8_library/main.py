from project.library import Library
from project.user import User
from project.registration import Registration

user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
print(registration.add_user(user, library))
registration.remove_user(user, library)
print(registration.remove_user(user, library))
registration.add_user(user, library)
print(registration.change_username(2, 'Igor', library))
print(registration.change_username(12, 'Peter', library))
print(registration.change_username(12, 'George', library))

[print(f'{user_record.id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user)

second_user = User(13, 'Peter')
registration.add_user(second_user, library)
library.books_available.update({'L.T.Rowling': ['The Test', 'The Test']})
library.get_book('L.T.Rowling', 'The Test', 10, second_user)
library.get_book('L.T.Rowling', 'The Test', 12, user)
third_user = User(15, 'Mike')
registration.add_user(third_user, library)
print(library.get_book('L.T.Rowling', 'The Test', 16, third_user))
print(library.books_available)
print(library.rented_books)
print(second_user)
print(registration.change_username(21, 'Pesho', library))

