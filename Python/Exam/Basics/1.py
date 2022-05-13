num_paper = int(input())
num_fabric = int(input())
num_glue = float(input())
discount = int(input())

paper = 5.8
fabric = 7.2
glue = 1.2

result = (num_paper * paper + num_fabric * fabric + num_glue * glue)
with_discount = result - result * (discount / 100)

print(f'{with_discount:.3f}')