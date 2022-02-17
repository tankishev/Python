# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. 
# Your job is to create a program to crack the codes. 
# On the first line of the input, you will receive the encrypted message. 
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations 
# that need to be performed upon the concealed message to interpret it and reveal its true content. 
# There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# 
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# 
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

message = input()

while True:
    line_input = input()
    if line_input == 'Decode':
        break
    
    instructions = line_input.split('|')

    if instructions[0] == 'Move':
        num = int(instructions[1])
        message = message[num:] + message[:num]

    elif instructions[0] == 'Insert':
        i = int(instructions[1])
        value = instructions[2]
        if 0 <= i:
            message = message[:i] + value + message[i:]

    elif instructions[0] == 'ChangeAll':
        old_chars = instructions[1]
        new_chars = instructions[2]
        message = message.replace(old_chars,new_chars)

print(f'The decrypted message is: {message}')