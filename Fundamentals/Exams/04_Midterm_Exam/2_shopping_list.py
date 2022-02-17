# It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"


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