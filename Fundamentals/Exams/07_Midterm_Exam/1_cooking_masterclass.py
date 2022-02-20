from math import ceil

budget = float(input())
students = int(input())
flour_num = students - students // 5
flour_price = float(input())
eggs_num = students * 10
eggs_price = float(input())
aprons_num = int(ceil(1.2 * students))
aprons_cost = float(input())

total_cost = flour_num * flour_price + eggs_num * eggs_price + aprons_num * aprons_cost

if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{abs(budget-total_cost):.2f}$ more needed.")
