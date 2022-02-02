# You will be given two strings. Transform the first string into the second one, letter by letter. Print only the unique strings.
# Note: the strings will have the same lengths.
# Input	Output
# bubble gum
# turtle hum	
# 
# tubble gum
# turble gum
# turtle gum
# turtle hum
# 
# Kitty
# Doggy	
# 
# Ditty
# Dotty
# Dogty
# Doggy


a = input()
b = input()
prt = ''
for i in range(len(a)):
    res = b[:i+1] + a[i+1:]
    if a[i] != b[i]:
        print(res)
