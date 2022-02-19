n = int(input())
output = 'Nothing found'

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(10):
            for d in range(9, c - 1, -1):
                num_sum = a + b + c + d
                num_prod = a * b * c * d

                if num_sum == num_prod and n % 10 == 5:
                    output = a * 1000 + b * 100 + c * 10 + d
                    print(output)
                    exit()

                elif num_prod // num_sum == 3 and n % 3 == 0:
                    output = d * 1000 + c * 100 + b * 10 + a
                    print(output)
                    exit()

print(output)
