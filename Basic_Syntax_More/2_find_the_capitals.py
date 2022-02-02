# Write a program that takes a single string and prints a list of all the capital letters indices.

capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
input_str = input()
output = [i for i in range(len(input_str)) if input_str[i] in capitals]
print (output)