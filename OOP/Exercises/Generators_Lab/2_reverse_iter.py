class reverse_iter:

    def __init__(self, iter) -> None:
        self.iter = iter
        self.start = len(iter) -1
        
        
    def __iter__(self):
        return self

    def __next__(self) -> int:
        
        if self.start <= self.end:
            i = self.start 
            self.start += 1
            return i
        raise StopIteration()