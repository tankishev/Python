class vowels:

    __VOWELS = ("a", 'e', 'i', 'o', 'u', 'y')

    def __init__(self, input_str: str) -> None:
        self.__input_str = input_str
        self.__start = 0

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> str:
        while self.__start < len(self.__input_str):
            character = self.__input_str[self.__start]
            self.__start += 1
            if character.isalpha() and character.lower() in vowels.__VOWELS:
                return character
        else:
            raise StopIteration()


if __name__ == '__main__':
    my_string = vowels('Abcedifuty0o')
    for char in my_string:
        print(char)
