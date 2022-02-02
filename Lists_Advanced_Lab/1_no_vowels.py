# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.



vowels = ('a', 'o', 'u', 'e', 'i')
input_data = input()
output_list = [x for x in input_data if x.lower() not in vowels]
output = ''.join(output_list)

print (output)
