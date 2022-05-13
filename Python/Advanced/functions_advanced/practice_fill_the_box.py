def fill_the_box(*args):
    args = list(args)
    height = args[0]
    length = args[1]
    width = args[2]
    end_point = args.index("Finish")
    cubes = args[3:end_point]

    total_volume = height * length * width
    taken_volume = sum([int(i) for i in cubes])

    if total_volume > taken_volume:
        return f"There is free space in the box. You could put {total_volume - taken_volume} more cubes."
    else:
        return f"No more free space! You have {abs(taken_volume - total_volume)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
