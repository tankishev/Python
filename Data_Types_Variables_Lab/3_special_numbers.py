# Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False). 
# A number is special when the sum of its digits is 5, 7, or 11.
# Examples
# Input	Output
# 15	1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False
# 7 -> True
# 8 -> False
# 9 -> False
# 10 -> False
# 11 -> False
# 12 -> False
# 13 -> False
# 14 -> True
# 15 -> False
# 6	1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False

special_range = (5,7,11)
num = int(input())

for i in range(1, num + 1):
    str_i = str(i)
    char_sum = 0
    for j in range(len(str_i)):
        char_sum += int(str_i[j])
    is_special = True if char_sum in special_range else False
    print(f"{i} -> {is_special}")
