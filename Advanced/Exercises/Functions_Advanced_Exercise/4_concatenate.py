# Write a function called concatenate() that receives some strings, concatenates them, and returns the result.


def concatenate(*args):
    return ''.join([arg for arg in args])
