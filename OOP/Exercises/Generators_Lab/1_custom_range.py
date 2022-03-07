class custom_range:

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.start <= self.end:
            i = self.start 
            self.start += 1
            return i
        raise StopIteration()

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)