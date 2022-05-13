# Task 1
def first_three_multiples(num):
    return num * 3

# Task 2
def tip(total, percentage):
    return total * (percentage / 100)

# Task 3
def introduction(first_name, last_name):
    concat = last_name + ", " + first_name + " " + last_name
    return concat

# Task 4
def dog_years(name, age):
    return f'{name}, you are {age * 7} years old in dog years'

# Task 5
def lots_of_math(a, b, c, d):
    e = a + b
    f = c - d
    g = e * f
    h = g % a
    print(e)
    print(f)
    print(g)
    return h