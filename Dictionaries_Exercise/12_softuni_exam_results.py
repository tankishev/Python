# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. 
# You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.

# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". 
# 
# You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". 
# In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# 
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# 
# Output
# •	Print the exam results for each participant
# •	After that, print each language in the format shown above
# •	Allowed working time / memory: 100ms / 16MB

exam_submissions = {}
students = {}

while True:
    input_line = input()
    if input_line == 'exam finished':
        break
    
    command = input_line.split('-')
    username = command[0]
    language_action = command[1]
    
    if language_action != 'banned':
        if language_action not in exam_submissions:
            exam_submissions[language_action] = 0
        exam_submissions[language_action] += 1

        points = int(command[2])
        students[username] = max(students.get(username, 0), points)
        
    elif username in students:
        students.pop(username)


print('Results:')
for username, points in students.items():
    print(f"{username} | {points}")
print('Submissions:')
for language, submissions_count in exam_submissions.items():
    print(f'{language} - {submissions_count}')
