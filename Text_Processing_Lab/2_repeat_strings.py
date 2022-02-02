# Write a program which reads a sequence of strings, separated by a single space. 
# Each string should be repeated N times, where N is the length of the string. 
# Print the final strings concatenated into one string.

words = input().split(' ')
output = ''
for word in words:
    output += word * len(word)
print(output)