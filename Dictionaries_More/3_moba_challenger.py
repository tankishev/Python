# You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, 
# else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him. 
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players, 
# ordered by total skill in descending order, then ordered by player name in ascending order. 
# For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"


tier = {}       #tier {player: {position: skill}}

while True:
	input_line = input()
	if input_line == 'Season end':
		break
	
	if ' -> ' in input_line:
		player, possition, skill = input_line.split(' -> ')
		
		if player not in tier:
			tier[player] = {possition: int(skill)}
			
		elif possition not in tier[player].keys():
			tier[player][possition] = int(skill)
		
		else:
			tier[player][possition] = max(tier[player][possition], int(skill))
		
	elif ' vs ' in input_line:
		p1, p2 = input_line.split(' vs ')
		
		if p1 in tier.keys() and p2 in tier.keys():	
			for p1_position in tier[p1].keys():
				if p1_position in tier[p2].keys():
					p1_skill = sum(tier[p1].values())
					p2_skill = sum(tier[p2].values())
					if p1_skill < p2_skill:
						tier.pop(p1)
					elif p2_skill < p1_skill:
						tier.pop(p2)
					break

player_pts = [(p, sum(tier[p].values())) for p in tier.keys()]
player_ranking = [rank for rank in sorted(player_pts, key= lambda item: (-item[1], item[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(tier[player].items(), key= lambda item: (-item[1], item[0]))]
    output = [f'- {pos} <::> {skill}' for pos, skill in position_ranking]
    print(*output, sep='\n')