def read_next(*args) -> iter:
    for arg in args:
        for el in arg:
            yield el

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
