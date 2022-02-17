def put_char(position, max_positions, large_ok, spec_ok, num_ok):
    global temp_txt
    global text_file
    global combs
    my_chars = list(chars_small)
    my_large_ok = large_ok
    my_specs_ok = spec_ok
    my_nums_ok = num_ok

    if my_large_ok: my_chars.extend(chars_large)
    if my_specs_ok: my_chars.extend(chars_spec)
    if my_nums_ok: my_chars.extend(chars_num)

    if position < max_positions:
        i = position
        for x in my_chars:

            temp_pass[i] = x
            my_large = len([x for x in temp_pass if x in chars_large])
            my_num = len([x for x in temp_pass if x in chars_num])
            my_specs = len([x for x in temp_pass if x in chars_spec])

            if my_large <= max_large:
                if my_num <= max_num:
                    if my_specs <= max_spec:
                        if not (x in chars_spec and temp_pass.count(x) > same_specs):
                            if temp_pass.count(x) <= max_rept:
                                print_pass = ''.join(temp_pass)
                                #text_file.write(f'{print_pass}\n')
                                print(print_pass)
                                combs += 1
                                if combs % 1000000 == 0:
                                    print(f'{combs * 100/status[lenght]:.0f}% done')

            if position < max_positions - 1:
                next_position = position + 1
                put_char(next_position, max_positions, my_large < max_large, my_specs < max_spec, my_num < max_num)
                
            #    for j in range(i + 1, max_positions):
            #        temp_pass[j] = chars[0]
            # print_pass = ''.join(temp_pass)
            # if temp_txt != print_pass:
            #     temp_txt = print_pass
            #     print(print_pass)
            #     #text_file.write(f'{print_pass}\n')

chars_apha = [chr(x) for x in range(128) if chr(x).isalpha()]
chars_small = tuple(x for x in 'abcdefghijklmnopqrstuvwxyz')
chars_large = tuple(x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
chars_num = tuple(x for x in '0123')  
chars_spec = tuple(x for x in '.!@#$')

chars = []
chars.extend(chars_small)
chars.extend(chars_large)
chars.extend(chars_num)
chars.extend(chars_spec)

status = {6: 309, 7:8032, 8:208827}


lenght = 4
max_num = 1#4
max_spec = 1#3
max_large = 1#2

same_specs = 1
max_rept = 3
combs = 0

temp_large = [0 for x in range(lenght)]





temp_pass = [' ' for _ in range(lenght)]
temp_txt = ''

#text_file = open("c:/testPY.txt", "w")
put_char(0,lenght, True, True, True)
#text_file.close()
