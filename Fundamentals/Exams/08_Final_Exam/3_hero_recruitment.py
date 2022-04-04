heroes = {}
while True:
    input_line = input()
    if input_line == 'End':
        break

    command_args = input_line.split(' ')
    command, hero_name = command_args[0], command_args[1]

    if command == 'Enroll':
        if hero_name in heroes.keys():
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command == 'Learn':
        if hero_name in heroes.keys():
            spell = command_args[2]
            spell_book = heroes.get(hero_name)
            if spell in spell_book:
                print(f"{hero_name} has already learnt {spell}.")
            else:
                spell_book.append(spell)
        else:
            print(f"{hero_name} doesn't exist.")

    elif command == 'Unlearn':
        if hero_name in heroes.keys():
            spell = command_args[2]
            spell_book = heroes.get(hero_name)
            if spell in spell_book:
                spell_book.remove(spell)
            else:
                print(f"{hero_name} doesn't know {spell}.")
        else:
            print(f"{hero_name} doesn't exist.")

print('Heroes:')
for hero in heroes.keys():
    spells = heroes.get(hero, [])
    spells_list = ''
    if len(spells) > 0:
        spells_list = ' ' + ', '.join(spells)
    print(f'== {hero}:{spells_list}')
