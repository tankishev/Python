# Write a program that prints the sum of all found characters between two given characters (their ASCII code). 
# On each of the first two lines, you will receive a single character. On the last line, you get a random string. 
# Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.

ch1_ascii_num = ord(input())
ch2_ascii_num = ord(input())
input_string = input()

sum_of_ascii = sum([ord(x) for x in input_string if ch1_ascii_num < ord(x) < ch2_ascii_num])

print(sum_of_ascii)