# Create a class called Profile. Upon initialization it should receive:
# •	username: str - the username should be between 5 and 15 characters (inclusive).
# If it is not, raise a ValueError with message "The username must be between 5 and 15 characters."
# •	password: str - the password must be at least 8 characters long; it must contain at least one upper
# case letter and at least one digit. If it does not, raise a ValueError with message
# "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
# Hint: Use Getters and Setters to name mangle them.
# Override the __str__() method of the base class so it returns:
# "You have a profile with username: "{username}" and password: {"*" with the length of password}".


class Profile:

    def __init__(self, username: str, password: str) -> None:
        self.user = username
        self.password = password

    @property
    def user(self):
        return self.__username

    @user.setter
    def user(self, user_name: str):
        if 5 <= len(user_name) <= 15:
            self.__username = user_name
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return f'{"*" * len(self.__password)}'

    @password.setter
    def password(self, pass_word: str):
        if len(pass_word) >= 8 \
                and len([x for x in pass_word if x.isnumeric()]) > 0 \
                and len([x for x in pass_word if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) > 0:

            self.__password = pass_word
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
