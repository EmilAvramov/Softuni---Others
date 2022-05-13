count = int(input())


def triple_fibonacci(_count):
    list_numbers = [1, ]
    for i in range(1, len(list_numbers) + _count - 1):
        list_numbers.append(sum(list_numbers[-3:]))
    return list_numbers


print(*triple_fibonacci(count), sep=' ')
