collection = {}

for _ in range(int(input())):
    piece = input().split('|')
    name = piece[0]
    composer = piece[1]
    key = piece[2]
    
    collection[name] = {'composer': composer, 'key': key}

while True:
    input_line = input()
    if input_line == 'Stop':
        break

    input_line = input_line.split('|')
    command = input_line[0]
    piece = input_line[1]

    if command == 'Add':
        composer = input_line[2]
        key = input_line[3]

        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == 'Remove':
        if piece in collection:
            collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == 'ChangeKey':
        new_key = input_line[2]
        
        if piece in collection:
            collection[piece]['key'] = new_key    
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_list = [s for s in sorted(collection.items(), key= lambda item: (item[0], item[1]['composer']))]
for item in sorted_list:
    print(f"{item[0]} -> Composer: {item[1]['composer']}, Key: {item[1]['key']}")