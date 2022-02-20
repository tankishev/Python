chat = []
while True:
    input_line = input().split()
    command = input_line[0]
    if command == 'end':
        break

    args = input_line[1:]

    if command == 'Chat':
        msg = args
        chat.extend(msg)

    elif command == 'Delete':
        msg = args[0]
        if msg in chat:
            chat.remove(msg)

    elif command == 'Edit':
        msg, new_msg = args[0], args[1]
        if msg in chat:
            chat[chat.index(msg)] = new_msg

    elif command == 'Pin':
        msg = args[0]
        if msg in chat:
            chat.append(chat.pop(chat.index(msg)))

    elif command == 'Spam':
        chat.extend(args)

print(*chat, sep='\n')