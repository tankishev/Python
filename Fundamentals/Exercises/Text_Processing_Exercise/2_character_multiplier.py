# Create a program that receives two strings on a single line separated by a single space. 
# Then, it prints the sum of their multiplied character codes as follows: 
# multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters. 
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

sum_of_multiplication = lambda x, y: sum([ord(x[i]) * ord(y[i]) for i in range(min(len(x),len(y)))])

def addition_of_remainder(x, y):
    diff = abs(len(x) - len(y))
    if len(x) > len(y):
        return sum([ord(ch) for ch in x[-diff:]])
    elif len (y) > len(x):
        return sum([ord(ch) for ch in y[-diff:]])
    else:
        return 0

strings = input().split(' ')
output = sum_of_multiplication(strings[0], strings[1]) + addition_of_remainder(strings[0],strings[1])
print (output)