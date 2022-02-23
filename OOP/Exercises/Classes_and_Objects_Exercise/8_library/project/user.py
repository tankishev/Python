# In the user.py file, create class User. Upon initialization, it should receive user_id (int) and username (string).
# The class should also have an instance attribute books that is an empty list.
# You should also create 2 instance methods:
# -	info() -    returns a string containing the books currently rented by the user in ascending order
#               separated by comma and space.
# -	__str__() - override the method to get a string in the following format
#               "{user_id}, {username}, {list of rented books}"


class User:

    def __init__(self, user_id: int, username: str) -> None:
        self.id = user_id
        self.username = username
        self.books = []

    def info(self) -> str:
        return ', '.join(sorted(self.books))

    def __str__(self) -> str:
        return f"{self.id}, {self.username}, {self.books}"
