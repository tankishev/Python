# As a young traveler, you gather items and craft new items.
# You will receive a journal with some Collecting items, separated with ", " (comma and space). 
# After that, until receiving "Craft!" you will be receiving different commands. 
# Commands (split by " - "):
# •	"Collect - {item}" – Receiving this command, you should add the given item to your inventory. If the item already exists, you should skip this line.
# •	"Drop - {item}" – You should remove the item from your inventory if it exists.
# •	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).


journal = input().split(', ')
while True:
    command = input()
    if command == 'Craft!':
        break
    else:
        args = command.split(' - ')

        if args[0] == 'Collect' and (args[1] not in journal):
            journal.append(args[1])
        
        elif args[0] == 'Drop' and (args[1] in journal):
            journal.remove(args[1])
        
        elif args[0] == 'Renew' and (args[1] in journal):
            journal.remove(args[1])
            journal.append(args[1])
        
        elif args[0] == 'Combine Items':
            oldItem, newItem = args[1].split(':')
            if oldItem in journal:
                journal.insert(journal.index(oldItem)+1,newItem)

output = ', '.join(journal)
print(output)