def add(a, b):
    j = b.split(", ")
    if j[1] not in a:
        a.append(j[1])
        print("Card successfully added")
    else:
        print("Card is already in the deck")
    return a


def insert(a, b):
    j = b.split(", ")
    if not 0 <= int(j[1]) < len(a):
        print("Index out of range")
    elif j[2] in a:
        print("Card is already added")
    elif 0 <= int(j[1]) < len(a) and j[2] not in a:
        a.insert(int(j[1]), j[2])
        print("Card successfully added")
    return a


def remove(a, b):
    j = b.split(", ")
    if j[1] in a:
        a.remove(j[1])
        print("Card successfully removed")
    elif j[1] not in a:
        print("Card not found")
    return a


def remove_at(a, b):
    j = b.split(", ")
    if not 0 <= int(j[1]) < len(a):
        print("Index out of range")
    elif 0 <= int(j[1]) < len(a):
        a.pop(int(j[1]))
        print("Card successfully removed")
    return a


cards = list(map(str, input().split(", ")))
number_commands = int(input())

for i in range(1, number_commands + 1):
    info = input()
    x = info.split(", ")

    if "Add" == x[0]:
        add(cards, info)
    if "Insert" == x[0]:
        insert(cards, info)
    if "Remove" == x[0]:
        remove(cards, info)
    if "Remove At" == x[0]:
        remove_at(cards, info)

print(*cards, sep=", ")
