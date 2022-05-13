data = [int(i) for i in input().split()]

positive = [i for i in data if i > 0]
negative = [i for i in data if i < 0]

print(sum(negative))
print(sum(positive))
if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
