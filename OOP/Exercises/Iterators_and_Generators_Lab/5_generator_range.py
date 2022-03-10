def genrange(start: int, end: int) -> iter:
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))
