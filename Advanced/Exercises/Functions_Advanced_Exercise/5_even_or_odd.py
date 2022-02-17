# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. 
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. 
# Submit only the function in the judge system.

def even_odd(*args):
    filter_ = {
        'even': lambda x: x % 2 == 0,
        'odd': lambda x: x % 2 != 0
    }

    return [arg for arg in args[:-1] if filter_[args[-1]](arg)]

