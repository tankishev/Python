# Write a program which receives a single string. On the first line it should print all the digits found in the string, 
# on the second – all the letters, and on the third – all the other characters. 
# There will always be at least one digit, one letter and one other characters.

txt_input = input()

print(''.join([ch for ch in txt_input if ch.isdigit()]))
print(''.join([ch for ch in txt_input if ch.isalpha()]))
print(''.join([ch for ch in txt_input if not (ch.isdigit() or ch.isalpha()) ]))
