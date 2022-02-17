#  You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
# Return a list containing all to-do notes sorted by importance in ascending order. 
# The importance value will always be an integer between 1 and 10 (inclusive).

# #solution without unique priorities
# command = input()
# ToDo_list = []

# while command != 'End':
#     ToDo_list.append(list(command.split('-'))) 
#     command = input()
# else:
#     ToDo_list.sort(key=lambda x: (x[0],x[1]))
#     print_list = [x[1] for x in ToDo_list]
#     print(print_list)

# solution with unique priorities
ToDo = [0] * 10
command = input()

while command != 'End':
    command_args = command.split('-')
    ToDo.pop(int(command_args[0])-1)
    ToDo.insert(int(command_args[0])-1,command_args[1])
    command = input()

else:
    output = [x for x in ToDo if x != 0]
    print (output)
