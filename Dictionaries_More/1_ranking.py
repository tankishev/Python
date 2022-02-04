# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. 
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. 
# 
# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". 
# Save that data because you will need it later. 
# 
# After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". 
# Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. 
# If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# 
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) 
# in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.
# 
# Input
# •	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
# •	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with same total points!
# 
# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points} 
# …
# #  {contestN} -> {points}"
# 
# Constraints
# •	The strings may contain any ASCII character except from (:, =, >).
# •	The numbers will be in range [0 - 10000].
# •	Second input is always valid.


contests = {}           # contests {contest: password}
submissions = {}        # submissions {user: {contest: points}}
group_ranking = []

while True:
    input_line = input()
    if input_line == 'end of contests':
        break

    contest, password = input_line.split(':')
    contests[contest] = password

while True:
    input_line = input()
    if input_line == 'end of submissions':
        break

    contest, password, user, pts = input_line.split('=>')

    if contest in contests and contests.get(contest) == password:
        
        if user in submissions and contest in submissions.get(user):
            current_points = submissions[user][contest]
            submissions[user][contest] = max(current_points, int(pts))

        elif user in submissions:
            submissions[user][contest] = int(pts)

        else:
            submissions[user] = {contest: int(pts)}

for user in submissions.keys():
    total_pts = sum(submissions[user].values())
    group_ranking.append((user,total_pts))

sorted_ranking = sorted(group_ranking, key=lambda item: -item[1])
print(f"Best candidate is {sorted_ranking[0][0]} with total {sorted_ranking[0][1]} points.")

sorted_users = sorted([user for user in submissions.keys()])

print('Ranking:')
for user in sorted_users:
    user_submissions = [u_s for u_s in sorted(submissions[user].items(), key=lambda item: -item[1])]
    output = [f'#  {contest} -> {points}' for (contest, points) in user_submissions]
    print(user)
    print(*output, sep='\n')

