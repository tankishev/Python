# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:


# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400

# You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level. If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
# •	If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle
# Input
# •	The first line of input will represent the values of boxes with materials - integers, separated by a single space
# •	On the second line, you will be given the magic values - integers again, separated by a single space
# Output
# •	On the first line - print whether you've succeeded in crafting the presents:
# o	"The presents are crafted! Merry Christmas!"
# o	"No presents this Christmas!"
# •	On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
# o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
# o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
# •	On the next lines print the presents you have crafted, ordered alphabetically in the format:
# o	"{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"



from collections import deque


crafting = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

finished_combo = (
    (150,250),
    (300,400)
)

def make_present(materials_data: list, magic_data: deque) -> str:
   
    magic, material = magic_data.popleft(), materials_data.pop()
            
    if magic * material in crafting: 
        return crafting.get(magic * material)
    elif magic * material < 0:
        materials_data.append(magic + material)
    elif magic * material > 0:
        materials_data.append(material + 15)
    elif magic * material == 0:
        if magic > 0: magic_data.appendleft(magic)
        if material > 0: materials_data.append(material)


def is_finished(presents: dict) -> None:
    finished = False
    
    for x, y in finished_combo:
        if crafting[x] in presents.keys() and crafting[y] in presents.keys():
            finished = True
            break
    if finished:
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")


def craft_presents(materials_data: list, magic_data: deque):
    
    crafted_presents = {}

    while materials_data and magic_data:
        toy = make_present(materials_data, magic_data)
        if toy:
            if not toy in crafted_presents:
                crafted_presents[toy] = 0
            crafted_presents[toy] += 1
        
    is_finished(crafted_presents)

    if materials_data:
        materials_data.reverse()
        print(f"Materials left:", ', '.join(list(map(str, materials_data))))
    if magic_data:
        print(f"Magic left:", ', '.join(list(map(str, magic_data))))
    toys = [f'{toy_name}: {amount}' for toy_name, amount in sorted(crafted_presents.items(), key=lambda item: item[0])]
    print(*toys, sep='\n')


materials_data = list(map(int, input().split()))
magic_data = deque(map(int, input().split()))
craft_presents(materials_data, magic_data)

