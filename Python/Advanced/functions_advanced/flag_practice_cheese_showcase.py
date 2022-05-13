def sorting_cheeses(**kwargs):
    sorted_list = []
    length_dict = {len(v) for v in kwargs.values()}
    if len(length_dict) <= len(kwargs) - 1:
        kwargs = sorted(kwargs.items(), key=lambda x: x)
    else:
        kwargs = sorted(
            kwargs.items(),
            key=lambda x: sum(int(i) for i in x[1]),
            reverse=True,
        )
    for item in kwargs:
        sorted_list.append([[item[0]], sorted(item[1], reverse=True)])
    sorted_list = [i for elem in sorted_list for i in elem]
    sorted_list = [
        str(i) if isinstance(i, int) else i
        for elem in sorted_list
        for i in elem
    ]
    return "\n".join(sorted_list)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
