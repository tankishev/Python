def check_the_material():
    text_with_materials = input()
    text_with_materials += ' ' + input()
    text_with_materials += ' ' + input()
    text_with_materials = text_with_materials.split()
    #text_with_materials = input().split()
    key_materials = {'shards': "Shadowmourne", 'fragments': "Valanyr", 'motes': "Dragonwrath"}
    my_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    for couple in range(0, len(text_with_materials), 2):
        quantity = int(text_with_materials[couple])
        material = text_with_materials[couple + 1].lower()
        if material in my_dict:
            my_dict[material] += quantity
        else:
            my_dict[material] = quantity
        if my_dict[material] > 250 and material in key_materials:
            my_dict[material] = my_dict[material] - 250
            print(f"{key_materials[material]} obtained!")
            break
        else:
            continue
    for key, value in my_dict.items():
        print(f"{key}: {value}")
 
check_the_material()