# Write a program that finds all integer and floating-point numbers in a string.
# Compose the Regular Expression
# A number has the following characteristics:
# •	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind). 
# The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
# •	The number might or might not be negative, so it might have a hyphen on its left side ("-").
# •	It consists of one or more digits.
# •	Might or might not have digits after the decimal point
# •	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
# •	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead). The syntax for the end of the RegEx might look something like "($|(?=\s))".

import re
input_string = input()
match_pattern = r'(^|(?<=\s))-?(0(\.d+)?|[1-9](\d+)?(\.\d+)?)($|(?=\s))'

matches = re.finditer(match_pattern,input_string)
for m in matches:
    print(m.group(0), end=' ')