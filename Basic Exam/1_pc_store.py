cpu_cost = float(input())
gpu_cost = float(input())
ram_cost = float(input())
ram_num = int(input())
discount = float(input())

total_cost = (1 - discount) * (cpu_cost + gpu_cost) + ram_num * ram_cost
total_bgn = total_cost * 1.57

print(f'Money needed - {total_bgn:.2f} leva.')
