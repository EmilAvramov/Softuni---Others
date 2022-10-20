def grocery_store(**kwargs):
    products = {}
    for (key, value) in kwargs.items():
        if key in products:
            products[key] += value
        else:
            products[key] = value

    products = dict(
        sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    )
    return "\n".join(f"{key}: {value}" for key, value in products.items())


print(grocery_store(bread=5, pasta=12, eggs=12,))
print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1,))
