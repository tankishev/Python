# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.


def mutate_data(data_type,data):
    if data_type == 'int':
        output = int(data) * 2
    elif data_type == 'real':
        output = float(data) * 1.5
        output = '{:.2f}'.format(output)
    elif data_type == 'string':
        output = '$' + data + '$'
    
    return output

output = mutate_data(input(),input())
print(output)