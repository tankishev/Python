# Write a program that reads a text from the console and counts the occurrences of each character in it. 
# Print the results in alphabetical (lexicographical) order.  

input_chars = [x for x in input()]
unique_chars = set(input_chars)
s = sorted(unique_chars)
output = ('{0}: {1} time/s'.format(x, input_chars.count(x)) for x in s)
print (*output, sep='\n')