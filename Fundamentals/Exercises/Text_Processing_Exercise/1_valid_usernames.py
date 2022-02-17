# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines. 
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

import string

valid_chars = [ch for ch in list(string.printable) if ch.isalnum() or ch in ('-','_')]

lenght_valid = lambda x: True if 3 <= len(x) <= 16 else False

found_invalid_char = lambda x: True if list(filter(lambda ch: ch not in valid_chars, x)) else False
    
usernames = input().split(', ')
for name in usernames:
    if lenght_valid(name) and not found_invalid_char(name):
        print(name)
