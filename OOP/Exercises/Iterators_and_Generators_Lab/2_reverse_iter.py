class reverse_iter:

    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.start = len(iterable)
        
    def __iter__(self) -> iter:
        return self

    def __next__(self) -> int:
        if self.start > 0:
            self.start -= 1
            return self.iterable[self.start]
        raise StopIteration()


if __name__ == '__main__':
    reversed_list = reverse_iter([1, 2, 3, 4])
    for item in reversed_list:
        print(item)
