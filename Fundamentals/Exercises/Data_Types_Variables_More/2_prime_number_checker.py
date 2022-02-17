# Write a program to check if a number is prime. A prime number is a natural number greater than 1, not a product of two smaller natural numbers. 
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.

number = int(input())

if number > 1:
    divisors_list = [x for x in range(2,(number+1)//2 + 1) if (number % x) == 0]
    if not divisors_list:
        print (True)
    else:
        print (False)
else:
    print (False)