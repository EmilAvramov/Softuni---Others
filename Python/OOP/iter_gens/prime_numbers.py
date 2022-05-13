def get_primes(_list: list):
    non_primes = []
    for a in _list:
        if a > 1:
            for i in range(2, a):
                if a % i == 0:
                    non_primes.append(a)
                    break
    for a in _list:
        if a not in non_primes and a != 0 and a != 1:
            yield a


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
