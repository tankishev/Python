# Write a program that reads the path to a file and subtracts the file name and its extension.

file_path = input()

rightmost_index = lambda x, y: max([i for i in range(len(x)-1,-1,-1) if x[i]==y])

ext_index = rightmost_index(file_path, '.')

file_ext = file_path[ext_index + 1:]

file_index = rightmost_index(file_path,'\\') + 1

file_name_lenght = ext_index - file_index

file_name = file_path[file_index:file_index + file_name_lenght]

print(f'File name: {file_name}')
print(f'File extension: {file_ext}')

