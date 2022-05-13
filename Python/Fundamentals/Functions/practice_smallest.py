a = int(input())
b = int(input())
c = int(input())


def smallest_of_three(x, y, z):
    if x < y and x < z:
        output = x
    elif y < z and y < x:
        output = y
    elif z < x and z < y:
        output = z
    else:
        output = "Error"
    return output


print(smallest_of_three(a, b, c))
