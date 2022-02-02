# Write a program to match full names from a sequence of characters and print them on the console.
# Writing the Regular Expression
# First, write a regular expression to match a valid full name, according to these conditions:
# 
# •	A valid full name has the following characteristics:
# o	It consists of two words.
# o	Each word starts with a capital letter.
# o	After the first letter, it only contains lowercase letters.
# o	Each of the two words should be at least two letters long.
# o	A single space separates the two words.


import re

intpu_string = input()
re_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(re_pattern,intpu_string)
output = ' '.join(matches)
print(output)