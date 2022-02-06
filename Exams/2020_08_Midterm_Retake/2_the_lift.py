max_people = 4
queue = int(input())
lifts = [int(x) for x in input().split(' ')]

free_slots = len(lifts)*4 - sum(lifts)
if queue > free_slots:
    print(f"There isn't enough space! {queue - free_slots} people in a queue!")
    print(' '.join([str(max_people)] * len(lifts)))

elif queue == free_slots:
    print(' '.join([str(max_people)] * len(lifts)))

else: 
    for i in range(len(lifts)):
        while queue > 0:
            if lifts[i] < max_people:
                lifts[i] += 1
                queue -= 1
            else:
                break
        else: 
            break
    print("The lift has empty spots!")
    print(' '.join(str(i) for i in lifts))
