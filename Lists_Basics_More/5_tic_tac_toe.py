# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print "Second player won". Otherwise, print "Draw!".

def winner(list):
    s = set(list)
    if sum(list) == 6:
        print("Second player won")
        return 2
    elif len(s) == 1 and 1 in s:
        print('First player won')
        return 1
    else:
        return 0


str_1 = input()
str_2 = input()
str_3 = input()

row = lambda str_x: [int(x) for x in str_x.split(' ')]
r1 = row(str_1)
r2 = row(str_2)
r3 = row(str_3)

c1 = [r1[0],r2[0],r3[0]]
c2 = [r1[1],r2[1],r3[1]]
c3 = [r1[2],r2[2],r3[2]]

x1 = [r1[0],r2[1],r3[2]]
x2 = [r1[2],r2[1],r3[0]]

if winner(r1) == 0:
    if winner(r2) == 0:
        if winner(r3) == 0:
            if winner(c1) == 0:
                if winner(c2) == 0:
                    if winner(c3) == 0:
                        if winner(x1) == 0:
                            if winner(x2) == 0:
                                print('Draw!')
