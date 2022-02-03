# Write a program that counts all characters in a string except for space (" "). 
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

input_line = input()
chars = {}

for char in input_line:
    if char != ' ':
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

for char, count in chars.items():
    print(f"{char} -> {count}")