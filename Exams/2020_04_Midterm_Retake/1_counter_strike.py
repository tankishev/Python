energy = int(input())
kills = 0

while True:
    input_line = input()
    if input_line == 'End of battle':
        break

    dist = int(input_line)

    if energy >= dist:
        energy -= dist
        kills += 1

        if kills % 3 == 0:
            energy += kills
    else:
        print(f"Not enough energy! Game ends with {kills} won battles and {energy} energy")
        break

if input_line == 'End of battle':
    print(f"Won battles: {kills}. Energy left: {energy}")
