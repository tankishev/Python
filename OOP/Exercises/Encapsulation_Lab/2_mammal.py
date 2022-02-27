# Create a class called Mammal. Upon initialization it should receive a name, type and sound.
# Create class attribute called kingdom which should not be accessed outside the class and set it to be "animals".
# Create three more instance methods:
# -	make_sound() - returns a string in the format "{name} makes {sound}"
# -	get_kingdom() - returns the private kingdom attribute
# -	info() - returns a string in the format "{name} is of type {type}"


class Mammal:

    __kingdom = 'animals'

    def __init__(self, name: str, type: str, sound: str) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    @staticmethod
    def get_kingdom():
        return Mammal.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"
