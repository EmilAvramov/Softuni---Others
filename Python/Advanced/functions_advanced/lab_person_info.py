def get_info(**kwargs):
    name = ""
    town = ""
    age = 0
    for key in kwargs.keys():
        if key == "name":
            name = kwargs[key]
        elif key == "town":
            town = kwargs[key]
        else:
            age = kwargs[key]
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
