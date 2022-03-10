class take_skip:

    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.__return = 0

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> int:
        if self.count > 0:
            self.count -= 1
            self.__return += self.step
            return self.__return - self.step
        raise StopIteration()


if __name__ == '__main__':
    numbers = take_skip(2, 6)
    for number in numbers:
        print(number)

    numbers = take_skip(10, 5)
    for number in numbers:
        print(number)

