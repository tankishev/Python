# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), 
# separated by a single space. Print the result on the console.

chr_1 = input()
chr_2 = input()

index_chr_1 = ord(chr_1)
index_chr_2 = ord(chr_2)

chr_list = [chr(x) for x in range(index_chr_1 + 1,index_chr_2)]

output = ' '.join(chr_list)
print (output)