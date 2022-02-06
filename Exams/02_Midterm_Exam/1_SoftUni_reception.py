emp1_sph = int(input())
emp2_sph = int(input())
emp3_sph = int(input())
students = int(input())

capacity = emp1_sph + emp2_sph + emp3_sph
timerequired = 0
breaktime = 0

while students > 0:
    students -= capacity
    timerequired += 1
    breaktime += 1
    if breaktime == 3 and students > 0:
        breaktime = 0
        timerequired += 1

print (f"Time needed: {timerequired}h.")