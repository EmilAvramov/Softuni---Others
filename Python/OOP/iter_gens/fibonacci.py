def fibonacci():
    a, b = 0, 1
    while 1:
        fibonacci = a
        a = b
        b = fibonacci + a
        yield fibonacci


generator = fibonacci()
for i in range(10):
    print(next(generator))
