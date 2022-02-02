# You will receive a single number. 
# You should write a function that returns the sum of all even and all odd digits in a given number. 
# The result should be returned as a single string in the format: 
# 
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def sum_odd_even_digits(number):
    number_str = str(number)
    digits_list = [int(x) for x in number_str]
    sum_even = 0
    sum_odd = 0
    for x in digits_list:
        if (x % 2) == 0:
            sum_even += x
        else:
            sum_odd += x
        
    return "Odd sum = {1:.0f}, Even sum = {0:.0f}".format(sum_even,sum_odd)

input_number = int(input())

print(sum_odd_even_digits(input_number))