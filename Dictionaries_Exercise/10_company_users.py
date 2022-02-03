# Write a program that keeps the information about companies and their employees. 
# You will be receiving company names and an employees' id until you receive the command "End" command. 
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format: 
# "{company_name} -> {employee_id}".
# •	The input always will be valid.

company_eployees = {}

while True:
    input_line = input()
    if input_line == 'End':
        break

    company_name, employee_id = input_line.split(' -> ')

    if company_name in company_eployees:
        if not employee_id in company_eployees.get(company_name):
            company_eployees[company_name].append(employee_id)
    else:
        company_eployees[company_name] = [employee_id]

for company_name in company_eployees.keys():
    formated_list = [f'-- {emp_id}' for emp_id in company_eployees.get(company_name)]
    print(company_name)
    print(*formated_list, sep='\n')