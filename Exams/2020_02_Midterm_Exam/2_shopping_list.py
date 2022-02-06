groceries = input().split('!')
while True:
    input_line = input()
    if input_line == 'Go Shopping!':
        break

    tokens = input_line.split(' ')
    command = tokens[0]
    item = tokens[1]

    if command == 'Urgent':
        if item not in groceries:
            groceries.insert(0, item)

    elif command == 'Unnecessary':
        if item in groceries:
            groceries.remove(item)

    elif command == 'Correct':
        if item in groceries:
            new_item = tokens[2]
            groceries = [new_item if x == item else x for x in groceries]

    elif command == 'Rearrange':
        if item in groceries:
            groceries.append(groceries.pop(groceries.index(item)))

print(*groceries, sep=', ')