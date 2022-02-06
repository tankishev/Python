
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