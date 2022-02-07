# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. 
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# •	"Drive : {car} : {distance} : {fuel}":
# o	You need to drive the given distance, and you will need the given fuel to do that. 
# If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print: 
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
# o	Refill the tank of your car. 
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up. 
# o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession, 
# sorted by their mileage in descending order, then by their name in ascending order, in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# 
# Input/Constraints
# •	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# •	The fuel and distance amounts in the commands will never be negative.
# •	The car names in the commands will always be valid cars in your possession.
# 
# Output
# •	All the output messages with the appropriate formats are described in the problem description.



cars = {}
fuel_capacity = 75

for _ in range(int(input())):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while True:
    input_line = input()
    if input_line == 'Stop':
        break

    tokens = input_line.split(' : ')
    command, car = tokens[0], tokens[1]

    if command == 'Drive':
        dist, fuel = int(tokens[2]), int(tokens[3])
        if cars[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['mileage'] += dist
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {dist} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]['mileage'] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif command == 'Refuel':
        fuel = int(tokens[2])
        refill = min(fuel, fuel_capacity - cars[car]['fuel'])
        cars[car]['fuel'] += refill
        print(f"{car} refueled with {refill} liters")

    elif command == 'Revert':
        km = int(tokens[2])
        current_km = cars[car]['mileage']
        km_change = min(km, current_km - 10000)
        cars[car]['mileage'] -= km_change
        if current_km - km >= 10000:
            print(f"{car} mileage decreased by {km_change} kilometers")

s = sorted(cars.items(), key=lambda item: (-item[1]['mileage'], item[0]))
output = [f"{item[0]} -> Mileage: {item[1]['mileage']} kms, Fuel in the tank: {item[1]['fuel']} lt." for item in s]
print(*output, sep='\n')