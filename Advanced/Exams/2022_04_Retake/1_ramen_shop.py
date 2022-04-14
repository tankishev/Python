from collections import deque

bowls = deque([int(el) for el in input().split(', ')])
clients = deque([int(el) for el in input().split(', ')])

while bowls and clients:
    bow = bowls.pop()
    client = clients.popleft()

    if bow == client:
        continue
    elif bow > client:
        bow -= client
        bowls.append(bow)
    elif client > bow:
        client -= bow
        clients.appendleft(client)

if not clients:
    print("Great job! You served all the customers.")
    if bowls:
        bowls_left = ', '.join([str(el) for el in bowls])
        print(f"Bowls of ramen left: {bowls_left}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    clients_left = ', '.join([str(el) for el in clients])
    print(f"Customers left: {clients_left}")
