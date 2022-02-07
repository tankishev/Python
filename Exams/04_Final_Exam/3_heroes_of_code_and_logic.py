# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format: 
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"
# Input
# •	On the first line of the standard input, you will receive an integer n
# •	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
# •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.


def increase_stats(hero, hp_mp, amount, max_amount) -> int:
    result = min(amount, max_amount - party[hero][hp_mp])
    party[hero][hp_mp] += result
    return result


party = {}
max_hp = 100
max_mp = 200


for _ in range(int(input())):
    hero, hp, mp = input().split()
    party[hero] = {'hp': int(hp), 'mp': int(mp)}

while True:
    input_line = input()
    if input_line == 'End':
        break

    tokens = input_line.split(' - ')
    command, hero = tokens[0], tokens[1]

    if command == 'CastSpell':
        required_mp, spell = int(tokens[2]), tokens[3]
        current_mp = party[hero]['mp']
        if current_mp >= required_mp:
            party[hero]['mp'] -= required_mp
            print(f"{hero} has successfully cast {spell} and now has {current_mp - required_mp} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command == 'TakeDamage':
        dmg, attacker = int(tokens[2]), tokens[3]
        current_hp = party[hero]['hp']
        if current_hp > dmg:
            party[hero]['hp'] -= dmg
            print(f"{hero} was hit for {dmg} HP by {attacker} and now has {current_hp - dmg} HP left!")
        else:
            party.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif command == 'Recharge':
        amount = int(tokens[2])
        recharge = increase_stats(hero, 'mp', amount, max_mp)
        print(f"{hero} recharged for {recharge} MP!")        

    elif command == 'Heal':
        amount = int(tokens[2])
        heal = increase_stats(hero, 'hp', amount, max_hp)
        print(f"{hero} healed for {heal} HP!")   

for hero, stats in party.items():
    current_hp = stats['hp']
    current_mp = stats['mp']
    print(f'{hero}\n HP: {current_hp}\n MP: {current_mp}')
