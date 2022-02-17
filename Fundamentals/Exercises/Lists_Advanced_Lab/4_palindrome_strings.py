# On the first line, you will receive words separated by a single space. 
# On the second line, you will receive a palindrome. 
# 
# First, you should print a list containing all the found palindromes in the sequence. 
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

_is_palindrome = lambda x: True if x == ''.join([c for c in x[::-1]]) else False

word_list = [x for x in input().split(' ')]
palindrome = input()

palindrome_list = list(filter(_is_palindrome,word_list))
print(palindrome_list)

number = palindrome_list.count(palindrome)
print(f'Found palindrome {number} times')