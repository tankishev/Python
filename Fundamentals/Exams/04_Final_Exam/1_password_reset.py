raw_pass = input()
while True:
    input_line = input()
    if input_line == 'Done':
        break

    tokens = input_line.split(" ")
    command = tokens[0]

    if command == 'TakeOdd':
        raw_pass = ''.join([x for i, x in enumerate(raw_pass) if i % 2 != 0])
        print(raw_pass)
    
    elif command == 'Cut':
        i, j = int(tokens[1]), int(tokens[2])
        raw_pass = raw_pass[:i] + raw_pass[i + j:]
        print(raw_pass)

    elif command == 'Substitute':
        old_txt, new_txt = tokens[1], tokens[2]
        if old_txt in raw_pass:
            raw_pass = raw_pass.replace(old_txt,new_txt)
            print(raw_pass)
        else:
            print("Nothing to replace!")

print(f"Your password is: {raw_pass}")