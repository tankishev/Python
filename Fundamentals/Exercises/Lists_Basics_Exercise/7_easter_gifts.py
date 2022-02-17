# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. 
# 
# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# 
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# 
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".  
# 
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift. 
# 
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one. 
# 
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"

gift_list = input().split(' ')

data = input()
while data != 'No Money':
    command = data.split(' ')
    action = command[0]
    gift = command[1]

    if action == 'OutOfStock':
        gift_list[:] = ['None' if item == gift else item for item in gift_list]

    elif action == 'Required': 
        gift_index = int(command[2])
        if 0 < gift_index < len(gift_list):
            gift_list[gift_index] = gift

    elif action == 'JustInCase': 
        gift_list.pop()
        gift_list.append(gift)
    
    data = input()

else:
    if len(gift_list) > 0:
        output = ''
        for gift in gift_list:
            if gift != 'None':
                output += gift + ' '
        print(output)

