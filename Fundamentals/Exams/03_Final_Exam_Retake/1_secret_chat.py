# On the first line of the input, you will receive the concealed message. 
# After that, until the "Reveal" command is given, you will receive strings with instructions for different operations 
# that need to be performed upon the concealed message to interpret it and reveal its actual content. 
# There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string. 
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"


secret_msg = input()
while True:
    input_line = input()
    if input_line == 'Reveal':
        break

    tokens = input_line.split(':|:')
    command = tokens[0]

    if command == 'InsertSpace':
        i = int(tokens[1])
        if 0 <= i < len(secret_msg):
            secret_msg = secret_msg[:i] + ' ' + secret_msg[i:]
            print(secret_msg)

    elif command == 'Reverse':
        reverse_str = tokens[1]
        i = secret_msg.find(reverse_str)
        if i == -1:
            print('error')
        else:
            temp_msg = secret_msg[:i]
            temp_msg += secret_msg[i + len(reverse_str):]
            temp_msg += reverse_str[::-1]
            secret_msg = temp_msg
            print(secret_msg)

    elif command == 'ChangeAll':
        old_str = tokens[1]
        new_str = tokens[2]

        secret_msg = secret_msg.replace(old_str,new_str)
        print(secret_msg)
    
    

print(f"You have a new text message: {secret_msg}")