from collections import ChainMap

customer_info = {
    "name": "Dmitri Buyer",
    "age": "31",
    "address": "123 Python Lane",
    "phone_number": "5552930183",
}

shirt_dimensions = {"shoulder": 20, "chest": 42, "torso_length": 29}

pants_dimensions = {
    "waist": 36,
    "leg_length": 42.5,
    "hip": 21.5,
    "thigh": 25,
    "bottom": 18,
}

customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)
print(customer_data)
customer_size_data = customer_data.parents
print(customer_size_data)
