def recursive_vector(idx: int, vector: list):
    if idx == len(vector) - 1:
        return print("".join(vector))

    for i in range(2):
        vector[idx] = i
        recursive_vector(idx + 1, vector)


number = int(input())

recursive_vector(number, [])
