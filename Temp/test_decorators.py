import functools


def my_decorator(func):
    
    
    def inner(*args):
        if type(args[0]) == tuple:
            return [func(*arg) for arg in args]
        else: 
            return func(*args)
            
    return inner

@my_decorator
def my_sum(*args):
    return sum(args)


list_of_ints = [1,2,3]
list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]

print(my_sum(*list_of_ints))
print(my_sum(*list_of_tuples))
print(repr(my_sum))