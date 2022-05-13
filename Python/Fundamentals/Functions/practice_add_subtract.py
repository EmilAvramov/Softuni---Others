int_1 = int(input())
int_2 = int(input())
int_3 = int(input())


def add_and_subtract(x, y, z):
    def sum_numbers():
        return x + y

    def subtract():
        return sum_numbers() - z
    return subtract()


print(add_and_subtract(int_1, int_2, int_3))
