numbers = [int(i) for i in str(input()).split()]


def combined_function(x):
    return min(x), max(x), sum(x)


print(f'The minimum number is {combined_function(numbers)[0]}')
print(f'The maximum number is {combined_function(numbers)[1]}')
print(f'The sum number is: {combined_function(numbers)[2]}')
