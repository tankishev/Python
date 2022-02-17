# Write a recursive function called palindrome() that will receive a word and an index (always 0). 
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" 
# if the word is not a palindrome using recursion. Submit only the function in the judge system.


def palindrome(word, index_) -> str:
    def recursive(word, index_):
        if len(word) == index_:
            return ''
        if len(word) > 0:
            retval = word[-1] + str(recursive(word[:-1], index_))
        return retval

    retval = recursive(word, index_)
    if retval == word:
        return f'{word} is a palindrome'
    else: 
        return f'{word} is not a palindrome'