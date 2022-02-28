def type_check(type_arg):
    def inner(func):
        def wrapper(*args):
            if any(type(arg) != type_arg for arg in args):
                return 'Bad Type'
            return func(*args)
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
