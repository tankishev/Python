# You will receive two lines of input: 
# •	a list of employees' happiness as a string of numbers separated by a single space 
# •	a happiness improvement factor (single number).
# 
# Your task is to find out if the employees are generally happy in their office. 
# 
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"


happiness_list = list(map(int, input().split(' ')))
factor = int(input())
happiness_list = [x * factor for x in happiness_list]

total_employees = len(happiness_list)
average_happyness = sum(happiness_list)/total_employees
happy_employees = len(list(filter(lambda x: x>= average_happyness, happiness_list)))

if happy_employees * 2 > total_employees:
    print(f'Score: {happy_employees}/{total_employees}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{total_employees}. Employees are not happy!')

