def math_operations(*args, **kwargs):
    args = [int(i) for i in args]
    sequence = 1
    for number in args:
        if sequence == 1:
            kwargs["a"] += number
            sequence += 1
        elif sequence == 2:
            kwargs["s"] -= number
            sequence += 1
        elif sequence == 3:
            if number != 0:
                kwargs["d"] /= number
            sequence += 1
        elif sequence == 4:
            kwargs["m"] *= number
            sequence = 1
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
