tshirt_cost = float(input())
target_cost = float(input())
shorts_cost = tshirt_cost * 0.75
socks_cost = shorts_cost * 0.2
shoes_cost = 2 * (tshirt_cost + shorts_cost)
discount = 0.15

total_cost = tshirt_cost + shorts_cost + socks_cost + shoes_cost
total_cost *= (1 - discount)

if total_cost >= target_cost:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_cost:.2f} lv.')
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f'He needs {abs(total_cost-target_cost):.2f} lv. more.')
