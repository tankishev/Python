raw_key = input()
while True:
    input_line = input()
    if input_line == 'Generate':
        break

    tokens = input_line.split('>>>')
    command = tokens[0]

    if command == 'Contains':
        txt_str = tokens[1]
        if txt_str in raw_key:
            print(f"{raw_key} contains {txt_str}")
        else:
            print('Substring not found!')

    elif command == 'Flip':
        up_low, i1, i2 = tokens[1], int(tokens[2]), int(tokens[3])        
        temp_key = raw_key[:i1]
        if up_low == 'Upper':
            temp_key += raw_key[i1:i2].upper()
        elif up_low == 'Lower':
            temp_key += raw_key[i1:i2].lower()
        temp_key += raw_key[i2:]
        raw_key = temp_key
        print(raw_key)

    elif command == 'Slice':
        i1, i2 = int(tokens[1]), int(tokens[2])
        raw_key = raw_key[:i1] + raw_key[i2:]
        print(raw_key)
    
print(f'Your activation key is: {raw_key}')