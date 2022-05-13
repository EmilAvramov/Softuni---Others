words = str(input()).split()
palindrome = str(input())


def f_palindrome(_sequence):
    results = []
    for word in _sequence:
        if word == word[::-1]:
            results.append(word)
    return results


print(f_palindrome(words))
print(f'Found palindrome {f_palindrome(words).count(palindrome)} times')
