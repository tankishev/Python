# o	"route1||route2||route3…"
# o	"Travel {light-years}"
# o	"Enemy {enemy's armour}"
# o	"Repair {number of ammunition and fuel added}"
# o	"Titan"


travel_route = input().split('||')
fuel = int(input())
ammo = int(input())
distance = 0

for el in travel_route:
    if el == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break

    command, num = el.split()

    if command == 'Travel':
        distance = int(num)
        if fuel < distance:
            print("Mission failed.")
            break
        else:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")

    elif command == 'Enemy':
        armor = int(num)
        if ammo >= armor:
            ammo -= armor
            print(f"An enemy with {armor} armour is defeated.")
        elif fuel >= armor * 2:
            fuel -= armor * 2
            print(f"An enemy with {armor} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif command == 'Repair':
        fuel += int(num)
        ammo += int(num) * 2
        print(f"Ammunitions added: {int(num) * 2}.")
        print(f"Fuel added: {int(num)}.")
