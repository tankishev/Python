class Stack:

    def __init__(self) -> None:
        self.data = []

    def push(self, element: str) -> None:
        self.data.append(element)
    
    def pop(self) -> str:
        if self.data:
            return self.data.pop()

    def top(self) -> str:
        if self.data:
            return self.data[-1]
    
    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return '[' + ', '.join(self.data[::-1]) + ']'


