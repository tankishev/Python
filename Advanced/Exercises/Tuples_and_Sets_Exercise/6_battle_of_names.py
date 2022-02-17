# You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each letter in the name 
# and integer divide it to the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ". 
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set


odd_nums = set()
even_nums = set()

for i in range(1, int(input()) + 1):
    sum_ascii = sum([ord(x) for x in input()])
    num = sum_ascii // i
    if num % 2 == 0:
        even_nums.add(num)
    else:
        odd_nums.add(num)

sum_odd, sum_even = sum(odd_nums), sum(even_nums)

if sum_odd == sum_even:
    print(', '.join([str(x) for x in even_nums.union(odd_nums)]))
elif sum_odd > sum_even:
    print(', '.join([str(x) for x in odd_nums.difference(even_nums)]))
else:
    print(', '.join([str(x) for x in even_nums.symmetric_difference(odd_nums)]))