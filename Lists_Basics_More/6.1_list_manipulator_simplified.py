

input_data = input()

input_list = []
for x in input_data.split(' '):
    input_list.append(int(x))

input_command = input()
while input_command != 'end':
    command = []  
    for x in input_command.split(' '):
        command.append(x) 
   
    action = command[0]
    
    if action == 'exchange':
        index = int(command[1])
        if index < 0 or index > (len(input_list) - 1):   
            print('Invalid index')  
        else:
    
            temp_list = input_list[index+1:]
            temp_list.extend(input_list[:index+1]) 
            input_list = temp_list
    
    elif action in ('max','min'):
        even_odd = command[1]
        if even_odd == 'even':
            temp_list = []
            for x in input_list:
                if (x % 2) == 0:
                    temp_list.append(x)
        
        elif even_odd == 'odd':
            temp_list = []
            for x in input_list:
                if (x % 2) != 0:
                    temp_list.append(x)

        if temp_list: #measures if there are items in the temp list
            if action == 'max':
                temp_num = max(temp_list)
            elif action == 'min':
                temp_num = min(temp_list)

            output_list = []
            for i in range(len(input_list)-1,-1,-1):
                if input_list[i]==temp_num:
                    output_list.append(i)

            output = max(output_list)

            print(output)    
        else: 
            print('No matches')

    elif action in ('first','last'):
        num_count = int(command[1])
        even_odd = command[2]
        
        if even_odd == 'even':
            temp_list = []
            for x in input_list:
                if (x % 2) == 0:
                    temp_list.append(x)
        elif even_odd == 'odd':
            temp_list = []
            for x in input_list:
                if (x % 2) != 0:
                    temp_list.append(x)

        
        if num_count > len(input_list):
            print('Invalid count')
        else:
            if action == 'first':
                temp_list = temp_list[:num_count]
            elif action == 'last':
                temp_list = temp_list[-num_count:]
            print(temp_list)
    
    input_command = input()

else:
    print (input_list)