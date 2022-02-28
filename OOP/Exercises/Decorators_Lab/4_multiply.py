def multiply(times):

    def decorator(function):

        output = times * function
        return output

    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
