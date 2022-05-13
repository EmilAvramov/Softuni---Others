first = str(input())
second = str(input())


def char_function(a, b):
    char_list = []
    for i in range(ord(a) + 1, ord(b)):
        char_list.append(chr(i))
    return char_list


print(*char_function(first, second), sep=' ')
