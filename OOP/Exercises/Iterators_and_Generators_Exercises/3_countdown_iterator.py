class countdown_iterator:

    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> int:
        if self.count >= 0:
            self.count -= 1
            return self.count + 1
        raise StopIteration()


if __name__ == '__main__':
    iterator = countdown_iterator(10)
    for item in iterator:
        print(item, end=" ")
