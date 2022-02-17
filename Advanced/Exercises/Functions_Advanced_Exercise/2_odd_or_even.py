# On the first line, you will receive a command - "Odd" or "Even".
# You will receive a sequence of numbers (integers) on the second line, separated by a single space.
# •	If the command is "Odd", print the sum of the odd numbers multiplied by the count of all numbers.
# •	If the command is "Even", print the sum of the even numbers multiplied by the count of all numbers.


def odd_or_even(odd_even: str, *args) -> None:

    if odd_even == 'Odd':
        num_sum = sum([int(x) for x in args if int(x) % 2 != 0])
    elif odd_even == 'Even':
        num_sum = sum([int(x) for x in args if int(x) % 2 == 0])

    print(num_sum * len(args))


cmd = input()
nums = input().split()
odd_or_even(cmd, *nums)
