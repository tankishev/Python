def multiply(times):
    def decorator(function):
        def wrapper(number):
            return function(number) * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


output = add_ten(3)
print(output)
