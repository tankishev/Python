# Decorate any function to add memory of call args and returns


class AddMemory(object):
    def __init__(self,func) -> None:
        self._memory = []
        self._count = 0
        self._func = func
        self._func_name = func.__name__

    def __call__(self, *args) -> object:
        retval = self._func(*args)
        self._memory.append(retval)
        self._count += 1
        return retval


    def memory(self) -> list:
        return self._memory

    
    def stats(self) -> str:
        retval = f'Fuction name: {self._func_name}' +'\n'
        retval += f'Called: {self._count} times'  +'\n'
        retval += f'Retval memory: {self._memory}'
        return retval

sum = AddMemory(sum)

@AddMemory
def my_print(*args):
    return print(*args)

test_list = [1,2,3,4,5,6,7,8,9]
my_print(sum(test_list[:4]))
my_print(sum(test_list[4:]))
my_print(sum.memory())
print(sum.stats())

print('\n')
print(my_print.stats())