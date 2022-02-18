n = int(input())
happy_nums = []

for num in range(1000, 10000):
    n4 = num % 10
    n3 = num % 100 // 10
    n2 = num % 1000 // 100
    n1 = num // 1000
    if n1 == 0 or n2 == 0 or n3 == 0 or n4 == 0:
        continue
    if n1 + n2 == n3 + n4:
	    if n % (n1 + n2) == 0:
		    happy_nums.append(num)
              
print(*happy_nums, sep=' ')