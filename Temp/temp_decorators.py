def my_decorator(func):
    def inner(*args):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            return tuple(func(*arg) for arg in args)
        return func(*args)
            
    return inner


@my_decorator
def my_sum(*args):
    return sum(args)


list_of_ints = [1,2,3]
list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

print(my_sum(*list_of_ints))
print(my_sum(*list_of_tuples))
print(my_sum(*list_of_lists))
print(repr(my_sum))
