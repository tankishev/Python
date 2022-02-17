# Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) from which you will be able to form the following colors: 
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found. 
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
# •	Single line string
# Output
# •	The list with the collected colors


from collections import deque


colours_list = ('red', 'yellow', 'blue', 'orange', 'purple', 'green')
secondary_colours = {
    'orange': ['red','yellow'], 
    'purple': ['red','blue'], 
    'green': ['blue','yellow']
    }

def extract_colors(data: deque) -> list:
    extracted_colors = []

    while data:        
        l_str = data.popleft()
        r_str = ''
        if data: 
            r_str = data.pop()
        
        if l_str + r_str in colours_list:
            extracted_colors.append(l_str + r_str)
        elif r_str + l_str in colours_list:
            extracted_colors.append(r_str + l_str)
        else:
            if len(l_str) > 1: data.insert(len(data)//2, l_str[:-1])
            if len(r_str) > 1: data.insert(len(data)//2, r_str[:-1])

    else:
        return extracted_colors

def validate_secondary(data: list) -> list:

    for colour in data:
        if colour in secondary_colours:
            valid = False
            main_color = secondary_colours.get(colour)
            if main_color[0] in data and main_color[1] in data:
                    valid = True

            if not valid: 
                data.remove(colour)
    
    return data

def paint_colours(data: deque):
    colors_list = extract_colors(data)
    colors_list = validate_secondary(colors_list)
    print(colors_list)


input_line = deque(input().split(' '))
paint_colours(input_line)
