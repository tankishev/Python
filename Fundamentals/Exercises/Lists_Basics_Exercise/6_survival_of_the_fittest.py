# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones, 
# and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

data = input()
lst = [int(x) for x in data.split(' ')]

numbers_to_remove = int(input())

sorted_lst = sorted(lst)
keep_lst = sorted_lst[numbers_to_remove:]

res = ''
for num in lst:
    if num in keep_lst:
        res += str(num) + ', '

print(res[:-2])

