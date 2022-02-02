# On the first line, you will receive a sequence of numbers separated by a single space. 
# On the second line, you will receive a string. # Your task is to write a program that sends a 
# message only using chars from the given string. Each char the program adds to the message should be found by its index. 
# The index you are looking for is the sum of a number's digits from the sequence. 
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). 
# When you find a char, you should add it to the message and remove it from the string. It means that for the following index, the text will be with one character less.
# Print the final message.

input_numbers = input()
input_string = input()

_num_sum = lambda num_as_text: sum([int(char) for char in num_as_text])
numbers_list = [_num_sum(x) for x in input_numbers.split(' ')]

char_list = [x for x in input_string]

output = ''

for num in numbers_list:
    while num > len(char_list):  
        num -= len(char_list)  

    char = char_list.pop(num)
    output += char

print(output)