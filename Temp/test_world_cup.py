import random

games = []
teams = []
stats = {}

print("Welcome to the group stage of world cup 2022!") 
print("Please enter the four teams who is in the list!")

for i in range(4):
    name = input()
    teams.append(name)
    stats[name] = {'W': 0, 'D': 0, 'L': 0, 'G': 0, 'Pts': 0}

print("Your group of finalist is:")
print(*teams, sep=', ')

print("To proceed to the simulation type PLAY:")
action = input()
if action == "PLAY":
    for i in range(4):
        for j in range(i, 4):
            if i!=j:
                games.append((i, j))

    for i, j in games:
        teamA, teamB = teams[i], teams[j]
        teamA_goals = random.choice(range(1,6))
        teamB_goals = random.choice(range(1,6))

        stats[teamA]['G'] += teamA_goals - teamB_goals
        stats[teamB]['G'] += teamB_goals - teamA_goals

        if teamA_goals > teamB_goals:
            stats[teamA]['W'] += 1
            stats[teamB]['L'] += 1
            stats[teamA]['Pts'] += 3
        elif teamA_goals < teamB_goals:
            stats[teamA]['L'] += 1
            stats[teamB]['W'] += 1
            stats[teamB]['Pts'] += 3
        else:
            stats[teamA]['D'] += 1
            stats[teamB]['D'] += 1
            stats[teamA]['Pts'] += 1
            stats[teamB]['Pts'] += 1

        print(f"{teamA} {teamA_goals} : {teamB_goals} {teamB}")

    ranking = sorted(stats.items(), key=lambda item: (item[1]['Pts'],item[1]['G']), reverse=True)

    print("RESULTS")
    print("Team\tW\tD\tL\tGD\tPts")
    for rank in ranking:
        print(f"{rank[0]}\t{rank[1]['W']}\t{rank[1]['D']}\t{rank[1]['L']}\t{rank[1]['G']}\t{rank[1]['Pts']}")

    print('\n')

    for rank in ranking:
        print(f"{rank[0]} has {rank[1]['Pts']} points with goal diff {rank[1]['G']}")

else:
    print("Bye! See you next time")