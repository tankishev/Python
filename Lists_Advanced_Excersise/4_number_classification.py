# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", 
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number

input_numbers = [int(x) for x in input().split(', ')]
positive_numbers = [str(x) for x in input_numbers if x >= 0]
negative_numbers = [str(x) for x in input_numbers if x < 0]
even_numbers = [str(x) for x in input_numbers if (x % 2 ) == 0]
odd_numbers = [str(x) for x in input_numbers if (x % 2 ) != 0]


print('Positive: ' + ', '.join(positive_numbers))
print('Negative: ' + ', '.join(negative_numbers))
print('Even: ' + ', '.join(even_numbers))
print('Odd: ' + ', '.join(odd_numbers))
