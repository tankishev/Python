txt = input()
lst = txt.split()
total = 0

for i in range(len(lst)):
    lst[i]=int(lst[i])
    total += lst[i]

average = total / len(lst)
lst.sort(reverse=True)

result = ''
for i in range(len(lst)):
    if lst[i] > average:
        result += str(lst[i]) + ' '
    else:
        break
    if i == 4:
        break

if result == '':
    result = 'No'
    
print(result)