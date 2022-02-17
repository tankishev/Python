# Write a regular expression to match a valid phone number from Sofia. 
# After you find all valid phones, print them on the console, separated by a comma and a space ", ".

# Compose the Regular Expression
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it is followed by a number:
# o	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively). 
# •	The different parts are separated by either a space or a hyphen ('-').


import re

input_string = input()
match_pattern = r'(\+359)([\s-])(2\2\d{3}\2\d{4}\b)'
matches = re.findall(match_pattern,input_string)
output_list = [m[0] + m[1] + m[2] for m in matches]
output = ', '.join(output_list)
print(output)