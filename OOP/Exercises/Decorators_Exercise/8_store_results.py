import datetime as dt

class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        retval = self.func(*args, **kwargs)
        output = "[{}] Function '{}' was called. Result: {}\n".format(dt.datetime.now(), self.func.__name__, retval)
        f = open('results.txt', 'a')
        f.write(output)
        f.close()
        return retval


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


print(add(2, 2))
print(mult(6, 4))
