def fibonacci(n, cache=None):
    if cache is None:
        cache = {}

    if n < 3:
        return n
    else:
        retval = cache.get(n, None)
        if retval is None:
            retval = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
            cache[n] = retval
        return retval


print(fibonacci(int(input())))
