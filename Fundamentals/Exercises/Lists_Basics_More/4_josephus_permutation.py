# This problem takes its name from arguably the most important event in the life of the ancient historian Josephus. 
# According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. 
# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded 
# to kill one man of every three until one last man was left (and that it was supposed to kill himself to end the act).
#  Well, Josephus and another man were the last, and, as we now know every detail of the story, you may have correctly 
# guessed that they did not precisely follow through with the original idea.
# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# •	the list itself - numbers separated by a single space representing the people in the circle
# •	a number k
# People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and proceeds from left to right. 
# After a specified number of people are skipped, the k person is executed. The procedure is repeated with the remaining people, 
# starting with the next person, going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

def _index_loop(len, start_index, steps):
    start_index += 1
    steps -= 1
    while start_index + steps > len:
        start_index -= len
    else:
        return (start_index + steps - 1)

input_data = input()
kill_sequence = int(input())

alive_list = [int(x) for x in input_data.split(' ')]

killed_list = []
start_index = 0

while len(alive_list) > 1:
    kill_index = _index_loop(len(alive_list),start_index,kill_sequence)
    killed_list.append(alive_list.pop(kill_index))
    start_index = kill_index
else:
    killed_list.extend(alive_list)
    output = '[' + ','.join([str(x) for x in killed_list]) + ']'
    print(output)