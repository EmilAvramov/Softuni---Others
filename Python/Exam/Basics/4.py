num_models = int(input())

total_rating = 0
total_sales = 0

rating_scale = {'2': 0, '3': 0.5, '4': 0.7, '5': 0.85, '6': 1}

for sales in range(num_models):
    number = int(input())
    str_number = str(number)
    num_sales = int(str_number[0:-1])
    rating = int(str_number[-1])
    for key, value in rating_scale.items():
        if str(rating) in key:
            total_sales += num_sales * value
    total_rating += rating

print(f'{total_sales:.2f}')
print(f'{total_rating/num_models:.2f}')
