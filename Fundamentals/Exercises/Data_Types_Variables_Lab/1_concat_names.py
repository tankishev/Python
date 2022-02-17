# Write a program that reads two names and a delimiter. It should print the names joined by the delimiter.
# Examples
# Input	Output
# John
# Smith
# ->	John->Smith
# Jan
# White
# <->	Jan<->White
# Linda
# Terry
# =>	Linda=>Terry

name_1 = input()
name_2 = input()
delimiter = input()

print(name_1 + delimiter + name_2)
