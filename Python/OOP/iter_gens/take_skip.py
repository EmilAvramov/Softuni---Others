class take_skip:
    def __init__(self, _step: int, _count: int) -> None:
        self.step = _step
        self.count = _count
        self.iterations = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            self.iterations -= 1
            return 0
        elif self.iterations != 0:
            result = self.step * (self.count - self.iterations)
            self.iterations -= 1
            return result
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
