# You will receive a number representing the number of wagons a train has. 
# Create a list (train) with the given length containing only zeros. 
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.


train_num = int(input())
train = [0] * train_num

command = input()
while command != 'End':
    command_args = command.split(' ')
    if command_args[0] == 'add':
        people = int(command_args[1])
        train[-1] += people
    elif command_args[0] == 'insert':
        people = int(command_args[2])
        wagon = int(command_args[1])
        train[wagon] += people
    elif command_args[0] == 'leave':
        people = int(command_args[2])
        wagon = int(command_args[1])
        train[wagon] -= people

    command = input()
else:
    print(train)


