def fibonacci() -> iter:
    prior = 0
    current = 1
    yield 0
    yield 1
    while True:
        retval = prior + current
        prior, current = current, retval
        yield retval


generator = fibonacci()
for i in range(10):
    print(next(generator))
