def recursive_draw(n):
    if n == 0:
        return

    print(n * '*')
    recursive_draw(n-1)
    print(n * '#')


num = int(input())
recursive_draw(num)
