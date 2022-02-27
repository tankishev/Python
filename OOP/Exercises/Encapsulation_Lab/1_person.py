# Create a class called Person. Upon initialization it should receive name and age.
# Name mangle the name and the age attributes (should not be accessed outside the class).
# Create two instance methods called get_name and get_age to return the values of the private attributes.


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age
