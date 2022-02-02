# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. 
# Write a function that receives a list of positive integers, separated by comma and space ", ". 
# The function should check if each integer is a palindrome - True or False. Print the result.


def is_palindrome(input_string):
    num_list = [x for x in input_string.split(', ')]
    
    reverse = lambda x: x[::-1]

    for num in num_list:
        print (num == reverse(num))

input_string = input()
is_palindrome(input_string)