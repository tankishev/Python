# Write a program which receives a text and a string of banned words, separated by a comma and space ", ". 
# All words included in the ban list should be replaced with asterisks "*", equal to the word's length. 
# The ban list will be entered on the first input line and the text - on the second input line. 

ban_list = input().split(', ')
txt_string = input()

for word in ban_list:
    while word in txt_string:
        txt_string = txt_string.replace(word, '*' * len(word))

print(txt_string)