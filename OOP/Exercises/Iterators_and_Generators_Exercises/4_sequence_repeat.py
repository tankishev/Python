class sequence_repeat:

    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.__i = -1

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> str:
        if self.number > 0:
            self.number -= 1
            if self.__i == len(self.sequence) - 1:
                self.__i = -1
            self.__i += 1
            return self.sequence[self.__i]
        raise StopIteration()


if __name__ == '__main__':
    result = sequence_repeat('abc', 5)
    for item in result:
        print(item, end='')
