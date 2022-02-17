# Write a function called fill_the_box that receives a different number of arguments representing:
# •	the height of a box
# •	the length of a box
# •	the width of a box
# •	n-times a different number of cubes with exact size 1 x 1 x 1
# •	a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# •	If, at the end, there is free space left in the box, print:
# o	"There is free space in the box. You could put {free space in cubes} more cubes."
# •	If there is no free space in the box, print:
# o	"No more free space! You have {cubes left} more cubes."


def fill_the_box(h, l, w, *args):
    volume = h * l * w
    cubes = args[:args.index('Finish')]
    num_cubes = sum(cubes)
    diff = abs(volume - num_cubes)
    if volume > num_cubes:
        return f"There is free space in the box. You could put {diff} more cubes."
    else:
        return f'No more free space! You have {diff} more cubes.'
