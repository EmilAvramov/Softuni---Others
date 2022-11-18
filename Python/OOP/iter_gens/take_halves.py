def solution():
    def integers():
        base = 0
        while True:
            base += 1
            yield base

    def halves():
        halves = 0
        while True:
            halves += 0.5
            yield halves

    def take(n: int, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))

        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
