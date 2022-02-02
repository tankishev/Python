# On the first line, you will receive a single number n. 
# On the following n lines, you will receive integers. 
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). 
# Finally, print the result.

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))
command = input()


if command == 'even':
#    filtered_list = list(filter(lambda x: (x % 2) == 0 or lst == 0,lst)) # alternative option with lambda
    filtered_list = [x for x in lst if (x % 2) == 0 or lst == 0] # alternative option with list comprehension
    print(filtered_list)
elif command== 'odd':
#    filtered_list = list(filter(lambda x: (x % 2) != 0 and lst != 0,lst)) # alternative option
    filtered_list = [x for x in lst if (x % 2) != 0 and lst != 0]
    print(filtered_list)
elif command == 'negative':
#    filtered_list = list(filter(lambda x: x < 0,lst)) # alternative option
    filtered_list = [x for x in lst if x < 0]
    print(filtered_list)
elif command == 'positive':
#    filtered_list = list(filter(lambda x: x >= 0,lst)) # alternative option
    filtered_list = [x for x in lst if x >=0]
    print(filtered_list)

