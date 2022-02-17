# Write a program that extracts all elements from a given sequence of words present in it an odd number of times (case-insensitive).
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.

input_line = input().lower().split(' ')
input_dic = {}

for word in input_line:
    if word not in input_dic:
        input_dic[word] = 0
    input_dic[word] += 1

output = [key for key, value in input_dic.items() if value % 2 != 0]
print(*output, sep=' ')