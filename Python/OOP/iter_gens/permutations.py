from itertools import permutations


def possible_permutations(_list):
    for item in permutations(_list):
        yield list(item)


[print(n) for n in possible_permutations([1, 2, 3])]
