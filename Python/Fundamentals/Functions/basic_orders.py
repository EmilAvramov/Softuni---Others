product = str(input())
quantity = int(input())


def products(prod, qty):
    if prod == "coffee":
        output = qty * 1.5
    elif prod == "water":
        output = qty
    elif prod == "coke":
        output = qty * 1.4
    else:
        output = qty * 2
    return output


print(f'{products(product, quantity):.2f}')
