from math import ceil

def bonus_calc(attendance, lectures, bonus) -> int:
    if lectures == 0:
        return 0
    else:
        return attendance / lectures * (5 + bonus)

students = int(input())
lectures = int(input())
bonus = int(input())
attendance = []

for _ in range(students):
    attendance.append(int(input()))

student_bonuses = [bonus_calc(count, lectures, bonus) for count in attendance]

if student_bonuses:
    max_bonus = max(student_bonuses)
    addendance_count = attendance[student_bonuses.index(max_bonus)]
else:
    max_bonus = 0 
    addendance_count = 0

print(f"Max Bonus: {ceil(max_bonus):.0f}.")
print(f"The student has attended {addendance_count} lectures.")

