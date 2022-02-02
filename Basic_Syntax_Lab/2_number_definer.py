num = float(input())
if num == 0:
    print('zero')
else:
    if abs(num) < 1:
        size = 'small '
    elif abs(num) > 1000000:
        size = 'large '
    else:
        size = ''
    if num > 0:
        print(size + 'positive')
    else:
        print(size+'negative')