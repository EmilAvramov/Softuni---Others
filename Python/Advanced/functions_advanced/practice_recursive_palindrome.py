def palindrome(_word: str, _index: int):
    if _word == _word[::-1]:
        return f"{_word} is a palindrome"
    else:
        return f"{_word} is not a palindrome"

    # if palindrome(_word, 0) == palindrome(_word[::-1], 0):
    #     return f"{_word} is a palindrome"
    # elif palindrome(_word, 0) != palindrome(_word[::-1], 0):
    #     return f"{_word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
