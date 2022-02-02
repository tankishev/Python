# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...). 
# Your task is to create a function that returns a loading bar depending on the number you have received in the input. 
# Print the result on the console. For more clarification, see the examples below.

# Input	Output
# 30	30% [%%%.......]
#       Still loading...
# 50	50% [%%%%%.....]
#       Still loading...
# 100	100% Complete!
#       [%%%%%%%%%%]


def loading_bar(percent):
    symbols_num = percent // 10
    output = '[' + '%' * symbols_num + '.' * (10 - symbols_num) +']'
    return output

input_number = int(input())
bar_section = loading_bar(input_number)

if input_number != 100:
    output = '{0}% {1}\nStill loading...'.format(input_number,bar_section)
else:
    output = '100% Complete!\n{0}'.format(bar_section)

print(output)