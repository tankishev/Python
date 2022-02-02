found = False
while found == False:
    num = float(input())
    if num >= 1 and num <= 100:
        found = True
        print(f"The number {num} is between 1 and 100")