# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:


def generate_pyramid(size: int, inverted: bool = False) -> list:
    steps = [i for i in range(1, size + 1)]
    if inverted:
        steps.reverse()
    return [' ' * (size - i) + '* ' * i for i in steps]


def generate_rhombus(size: int) -> list:
    retval = generate_pyramid(size)
    retval.extend(generate_pyramid(size, True)[1:])
    return retval


n = int(input())
output = generate_rhombus(n)
print(*output, sep='\n')

