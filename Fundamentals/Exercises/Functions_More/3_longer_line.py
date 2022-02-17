# You will be given the coordinates of four points. The first and the second pair of points form two different lines. 
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to the center of the coordinate system (0, 0).
# You can reuse the method that you wrote for the previous problem. If the lines are of equal length, print only the first one. 
# The resulting coordinates must be formatted to the lower integer.

from math import sqrt

def format_point(pt_a):
    return (int(pt_a[0]//1), int(pt_a[1]//1))

def closer(pt_a, pt_b):
    dist_x = sqrt((pt_a[0] ** 2 ) + (pt_a[1] ** 2 ))
    dist_y = sqrt((pt_b[0] ** 2 ) + (pt_b[1] ** 2 ))
    if dist_x <= dist_y:
        output = format_point(pt_a)
    elif dist_y < dist_x:
        output = format_point(pt_b)
    return output

def line_lenght(pt_a, pt_b):
    diff_x = pt_a[0] - pt_b[0]
    diff_y = pt_a[1] - pt_b[1]
    dist = sqrt((diff_x ** 2 ) + (diff_y ** 2 ))
    return dist


pt_1 = (float(input()),float(input()))
pt_2 = (float(input()),float(input()))
pt_3 = (float(input()),float(input()))
pt_4 = (float(input()),float(input()))

line_a = line_lenght(pt_1,pt_2)
line_b = line_lenght(pt_3,pt_4)

if line_a >= line_b:
    if format_point(pt_1) == closer(pt_1,pt_2):
        print(f'{str(format_point(pt_1))}{str(format_point(pt_2))}')
    else:
        print(f'{str(format_point(pt_2))}{str(format_point(pt_1))}')
else:
    if format_point(pt_3) == closer(pt_3,pt_4):
        print(f'{str(format_point(pt_3))}{str(format_point(pt_4))}')
    else:
        print(f'{str(format_point(pt_4))}{str(format_point(pt_3))}')

