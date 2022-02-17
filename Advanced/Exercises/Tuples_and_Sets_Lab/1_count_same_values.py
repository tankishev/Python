# You will be given numbers separated by a space. 
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
# The number must be formatted to the first decimal point.

nums = list(map(float, input().split()))
unique_nums = []
for x in nums:
    if x not in unique_nums:
        unique_nums.append(x)

output = ((x, nums.count(x)) for x in unique_nums)
for number, count in output:
    print(f"{number} - {count} times")
