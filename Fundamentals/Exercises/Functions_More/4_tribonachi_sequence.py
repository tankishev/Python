# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. You will receive a positive integer number as input.


def tribonachi(x):
    num_list = [0,0,1]
    for _ in range(x - 1):
        num_list.append(sum(num_list[-3:]))
    return num_list[-x:]


num = int(input())
output = ' '.join([str(x) for x in tribonachi(num)])

print(output)