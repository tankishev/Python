input_string = input()

while True:

    input_line = input()
    if input_line == 'Done':
        break

    command_args = input_line.split(' ')
    command = command_args[0]

    if command == 'Change':
        char, replacement = command_args[1], command_args[2]
        input_string = input_string.replace(char, replacement)
        print(input_string)

    elif command == 'Includes':
        substring = command_args[1]
        print((substring in input_string))

    elif command == 'End':
        substring = command_args[1]
        test_string = input_string[-len(substring):]
        print((test_string == substring))

    elif command == 'Uppercase':
        input_string = input_string.upper()
        print(input_string)

    elif command == 'FindIndex':
        char = command_args[1]
        print(input_string.find(char))

    elif command == 'Cut':
        startIndex, count = command_args[1], command_args[2]
        input_string = input_string[int(startIndex): (int(startIndex) + int(count))]
        print(input_string)




