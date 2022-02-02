# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.

import re

while True:
    input_text = input()
    if len(input_text) != 0:
        match_pattern = re.compile(r'\d+')
        matches = match_pattern.finditer(input_text)
        for match in matches:
            print(match.group(0), end=' ')
    else:
        break