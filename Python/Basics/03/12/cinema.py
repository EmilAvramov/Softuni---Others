movie_type = str(input())
n_rows = int(input())
n_columns = int(input())

area = n_rows * n_columns

if movie_type == "Premiere":
    profit = 12 * area
elif movie_type == "Normal":
    profit = 7.5 * area
else:
    profit = 5 * area

print(f'{profit:.2f}')



