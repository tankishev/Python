contests = {}   # contests {contest {username:points} }
users = {}      # users {username: total_points}

while True:
    input_line = input()
    if input_line == 'no more time':
        break
    
    username, contest, points = input_line.split(' -> ')

    if username not in users:
        users[username] = 0
    
    if contest in contests:
        if username in contests[contest]:
            current_points = contests[contest][username]
            contests[contest][username] = max(current_points, int(points))
            if current_points == int(points):
                users[username] += current_points
            else:
                users[username] += max(current_points, int(points)) - current_points
        else:
            contests[contest][username] = int(points)
            users[username] += int(points)
    else:
        contests[contest] = {username: int(points)}
        users[username] += int(points)

for contest in contests.keys():
    ranking = [rank for rank in sorted(contests[contest].items(), key=lambda item: (-item[1], item[0]))]
    output = [f'{i + 1}. {name} <::> {points}' for i, (name, points) in enumerate(ranking)]
    print(f"{contest}: {len(output)} participants")
    print(*output, sep='\n')

user_ranking = [rank for rank in sorted(users.items(), key=lambda item: (-item[1], item[0]))]
output = [f'{i + 1}. {name} -> {points}' for i, (name, points) in enumerate(user_ranking)]
print("Individual standings:")
print(*output, sep='\n')
