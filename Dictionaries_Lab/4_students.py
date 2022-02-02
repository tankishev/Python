# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}". 
# On the last line, you will receive a name of a course in snake case lowercase letters. 
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines. 

courses = {}
while True:
    input_data = input().split(':')
    if len(input_data) == 1:
        course = input_data[0]
        break
    else:
        name = input_data[0]
        id = input_data[1]
        course = '_'.join(input_data[2].split(' '))
        
        if course not in courses:
            courses[course] = []
        courses[course].append(f"{name} - {id}")

output_list = courses[course]
print(*output_list, sep= '\n')

