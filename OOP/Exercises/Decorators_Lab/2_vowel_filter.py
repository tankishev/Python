def vowel_filter(function):

    vowels = ["a", 'e', 'i', 'o', 'u', 'y']

    def wrapper():
        return [x for x in function() if x in vowels]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

output = get_letters()
print(output)
