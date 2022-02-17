# You are saying goodbye to your best friend: "See you next happy year". 
# Happy Year is the year with only distinct digits, for example, 2018. 
# Write a program that receives an integer number and finds the next happy year.

# Examples
# Input	Output
# 8989	9012
# 1001	1023

year = int(input())

while True:
    year += 1
    num_lst = list(str(year))
    num_len = len(num_lst)
    unique = True
    for _ in range(num_len):
        chr = num_lst.pop()
        if chr in num_lst:
            unique = False
            break
    if unique:
        break
print(year)

