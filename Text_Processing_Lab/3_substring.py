# On the first line you will receive a string. On the second line you will receive a second string. 
# Write a program which removes all the occurrences of the first string in the second until there is no match. 
# At the end print the remaining string.

remove_string = input()
text_string = input()

while remove_string in text_string:
    text_string = text_string.replace(remove_string,'')
else:
    print(text_string)
