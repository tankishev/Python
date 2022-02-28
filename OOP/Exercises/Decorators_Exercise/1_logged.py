def logged(function):
    def wrapper(*args):
        retval = f'you called {function.__name__}{args}\n'
        retval += f'it returned {function(*args)}'
        return retval
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))



