# Write a program which prints a set of elements.
# On the first line, you will receive two numbers - n and m, separated by a single space - they represent the lengths of two separate sets.
#  On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. 
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).

n, m = input().split()
set_a = set()
set_b = set()

for _ in range(int(n)):
    set_a.add(input())

for _ in range(int(m)):
    set_b.add(input())

output = set_a & set_b
print(*output, sep='\n')