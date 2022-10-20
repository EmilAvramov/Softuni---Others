def even_odd_filter(**kwargs):
    filter_dict = {}
    for (key, value) in kwargs.items():
        if key == "odd":
            value = [x for x in value if x % 2 != 0]
            filter_dict[key] = value
        else:
            value = [x for x in value if x % 2 == 0]
            filter_dict[key] = value
    filter_dict = dict(
        sorted(filter_dict.items(), key=lambda x: len(x[1]), reverse=True)
    )
    return filter_dict


print(
    even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    )
)
