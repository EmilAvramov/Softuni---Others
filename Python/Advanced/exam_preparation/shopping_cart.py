def shopping_cart(*args):
    def get_print(printable: dict):
        output = ""
        newline = "\n"
        missing = 0
        count = 0
        for key, value in printable.items():
            if len(value) > 0:
                if count == 0:
                    count += 1
                    output += f"{key}:\n{newline.join((' - ' + val) for val in value)}"
                else:
                    output += f"\n{key}:\n{newline.join((' - ' + val) for val in value)}"
            else:
                if count == 0:
                    count += 1
                    output += f"{key}:"
                else:
                    output += f"\n{key}:"
                missing += 1
        if missing == 3:
            return "No products in the cart!"
        return output

    def sort_dict(sortable: dict):
        result = {k: v.sort() for k, v in sortable.items()}
        result = dict(
            sorted(sortable.items(), key=lambda x: (-len(x[1]), x[0]))
        )
        return get_print(result)

    products = {"Soup": [], "Dessert": [], "Pizza": []}
    for arg in args:
        if arg == "Stop":
            return sort_dict(products)
        [meal, product] = arg
        if product not in products[meal]:
            if meal == "Pizza" and len(products[meal]) < 4:
                products[meal].append(product)
            if meal == "Soup" and len(products[meal]) < 3:
                products[meal].append(product)
            if meal == "Dessert" and len(products[meal]) < 2:
                products[meal].append(product)
    return sort_dict(products)


print(
    shopping_cart(
        ("Pizza", "ham"),
        ("Soup", "carrots"),
        ("Pizza", "cheese"),
        ("Pizza", "flour"),
        ("Dessert", "milk"),
        ("Pizza", "mushrooms"),
        ("Pizza", "tomatoes"),
        "Stop",
    )
)

print(
    shopping_cart(
        ("Pizza", "ham"), ("Dessert", "milk"), ("Pizza", "ham"), "Stop",
    )
)

print(shopping_cart("Stop", ("Pizza", "ham"), ("Pizza", "mushrooms"),))
