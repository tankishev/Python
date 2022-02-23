# In the registration.py, create a class called Registration. Upon initialization, It will not receive anything,
# but we'll have these three methods.
# -	add_user(user: User, library: Library):
# 	    Adds the user if we do not have them in the library's user records already
#       Otherwise, returns the message "User with id = {user_id} already registered in the library!"

# -	remove_user(user: User, library: Library):
#       Removes the user from the library records if present
#       Otherwise, returns the message "We could not find such user to remove!"

# -	change_username(user_id: int, new_username: str, library: Library):
#       If there is a record with the same user id in the library and the username is different than the provided one,
#       changes the username with the new one provided and returns the message "Username successfully changed
#       to: {new_username} for user id: {user_id}".
#       Changes his username in the rented_books dictionary as well (if present).

#       If the new username is the same for this id, returns the following message
#       "Please check again the provided username - it should be different than the username used so far!".

#       If there is no record for the provided id returns "There is no user with id = {user_id}!"


from .user import User
from .library import Library


class Registration:

    def __init__(self) -> None:
        pass

    # [?] what if same user_id exists
    # [?] what if same username exists
    def add_user(self, user: User, library: Library) -> str:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.id} already registered in the library!"

    # [?] What happens if there are records for rented books for this user
    def remove_user(self, user: User, library: Library) -> str:
        if user in library.user_records:
            library.user_records.remove(user)
            if user.username in library.rented_books.keys():
                library.rented_books.pop(user.username)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        matches = [user for user in library.user_records if user.id == user_id]
        if matches:
            user = matches[0]
            if user.username == new_username:
                return f"Please check again the provided username - " \
                       f"it should be different than the username used so far!"
            else:
                old_username = user.username
                user.username = new_username
                if old_username in library.rented_books.keys():
                    library.rented_books[new_username] = library.rented_books.pop(old_username)

                return f'Username successfully changed to: {new_username} for user id: {user_id}'
        else:
            return f"There is no user with id = {user_id}!"

