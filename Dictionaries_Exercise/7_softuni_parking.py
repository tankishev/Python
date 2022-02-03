# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. 
# It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# 
# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":
# o	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# o	If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# 
# •	"unregister {username}":
# o	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# o	If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# 
# After you execute all of the commands, print all the currently registered users and their license plates in the format: 
# •	"{username} => {license_plate_number}"
# 
# Input
# •	First line: n - number of commands - integer
# •	Next n lines: commands in one of the two possible formats:
# o	Register: "register {username} {license_plate_number}"
# o	Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.

parking_register = {}

for _ in range(int(input())):
    command = input().split(' ')
    action = command[0]
    user = command[1]

    if action == 'register':
        license_plate_number = command[2]
        if user in parking_register:
            print(f"ERROR: already registered with plate number {parking_register.get(user)}")
        else:
            parking_register[user] = license_plate_number
            print(f"{user} registered {license_plate_number} successfully")
    
    elif action == 'unregister':
        if user not in parking_register:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            parking_register.pop(user)

for username, license_plate_number in parking_register.items():
    print(f"{username} => {license_plate_number}")