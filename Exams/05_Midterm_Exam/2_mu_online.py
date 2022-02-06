health = 100
bitcoin = 0
rooms = input().split('|')
for i, room in enumerate(rooms):
    command, number = room.split(' ')
    if command == 'potion':
        healing = min(int(number), 100 - health)
        health += healing
        print(f"You healed for {healing} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoin += int(number)
        print(f"You found {number} bitcoins.")

    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i+1}")
            break

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")
