# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. 
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection, 
# sorted by their name and by the name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"

# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".

# Output
# •	All the output messages with the appropriate formats are described in the problem description.



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