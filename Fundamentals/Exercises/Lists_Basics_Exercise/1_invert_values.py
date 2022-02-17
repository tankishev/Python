# Write a program that receives a single string containing positive and negative numbers 
# separated by a single space. Print a list containing the opposite of each number.

data = input()
lst = data.split(' ')
res = [int(x)*-1 for x in lst]

print(res)

