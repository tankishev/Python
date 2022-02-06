stops = input()
while True:
    input_line = input()
    if input_line == 'Travel':
        break

    tokens = input_line.split(':')
    command = tokens[0]

    if command == 'Add Stop':
        i = int(tokens[1])
        stop = tokens[2]
        
        if 0 <= i < len(stops):
            stops = stops[:i] + stop + stops[i:]

        print(stops)
        
    elif command == 'Remove Stop':
        i = int(tokens[1])
        j = int(tokens[2])

        if 0 <= min(i,j) and max(i,j) < len(stops):
            stops = stops[:i] + stops[j+1:]
        
        print(stops)
        
    elif command == 'Switch':
        old_str = tokens[1]
        new_str = tokens[2]

        if len(old_str) > 0 and len(new_str) > 0:
            stops = stops.replace(old_str, new_str)
            print(stops)

print(f"Ready for world tour! Planned stops: {stops}")