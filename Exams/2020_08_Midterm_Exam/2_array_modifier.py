txt = input()
lst = [int(x) for x in txt.split()]

while True:
    txt = input()
    if txt == 'end':
        break
    elif txt == 'decrease':
        for i in range(len(lst)):
            lst[i] -= 1
    else:
        txt = txt.split()
        command = txt[0]
        index_1 = int(txt[1])
        index_2 = int(txt[2])

        if command == 'multiply':
            lst[index_1] *= lst[index_2]
        elif command == 'swap':
            tmp = lst[index_1]
            lst[index_1] = lst[index_2]
            lst[index_2] = tmp

result = ''
for i in range(len(lst)):
    result += str(lst[i]) + ', '

print(result[:-2])    