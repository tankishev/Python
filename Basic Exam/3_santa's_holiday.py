room_cost = {
    'room for one person': {'cost': 18, 'discount': (0, 0, 0)},
    'apartment': {'cost': 25, 'discount': (0.3, 0.35, 0.5)},
    'president apartment': {'cost': 35, 'discount': (0.1, 0.15, 0.2)}
}


def discount_index(days_: int) -> int:
    if days_ < 10:
        return 0
    elif 10 <= days_ <= 15:
        return 1
    elif days_ > 15:
        return 2


days = int(input())
room_type = input()
evaluation = input()

discount = room_cost[room_type]['discount'][discount_index(days)]
cost_of_stay = (days - 1) * room_cost[room_type]['cost'] * (1 - discount)

if evaluation == 'positive':
    cost_of_stay *= 1.25
else:
    cost_of_stay *= 0.9

print(f'{cost_of_stay:.2f}')