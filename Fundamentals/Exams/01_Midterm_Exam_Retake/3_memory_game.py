# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. 
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space, 
# representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, 
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a" 
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"

# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"

# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"


elements = input().split(' ')
moves = 0

while True:
    input_line = input()
    if input_line == 'end':
        break
    
    moves += 1
    indices = map(int, input_line.split(' '))
    a = next(indices)
    b = next(indices)
    
    if a == b or min(a, b) < 0 or max(a, b) >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        elem = f'-{moves}a'
        mid_index = len(elements) // 2
        elements = elements[:mid_index] + [elem]*2 + elements[mid_index:]
    
    else:
        if elements[a] == elements[b]:
            print(f"Congrats! You have found matching elements - {elements[a]}!")
            elements = [x for i, x in enumerate(elements) if i not in (a, b)]

            if not elements:
                print(f"You have won in {moves} turns!")
                break                
        else:
            print('Try again!')

if len(elements) > 0:
    print (f"Sorry you lose :(\n{' '.join(elements)}")