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