import math
shape = str(input())
if shape == "square":
    side_a = float(input())
    print(round((side_a*side_a), 3))
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(round((side_a * side_b), 3))
elif shape == "circle":
    radius = float(input())
    print(round((math.pi*radius*radius), 3))
else:
    side_a = float(input())
    height = float(input())
    print(round(((side_a * height)/2), 3))
