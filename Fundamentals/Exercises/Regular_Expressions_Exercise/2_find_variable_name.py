# Write a program that finds all variable names in each string. 
# A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. 
# Extract only their names without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.

import re
text = input()
pattern = re.compile(r'(^|(?<=\s))_([a-zA-Z0-9]+(?=\s|$))')
matches = re.finditer(pattern,text)

output = [m.group(2) for m in matches]
print(','.join(output))