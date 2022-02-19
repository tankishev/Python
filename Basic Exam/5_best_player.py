scoreboard = {}
while True:
    name = input()
    if name == 'END':
        break

    if name not in scoreboard:
        scoreboard[name] = 0
    scoreboard[name] += int(input())

    if scoreboard.get(name) >= 10:
        break

name, goals = next((el for el in sorted(scoreboard.items(), key=lambda item: -item[1])))
print(f'{name} is the best player!')
if goals >= 3:
    print(f'He has scored {goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {goals} goals.')
    