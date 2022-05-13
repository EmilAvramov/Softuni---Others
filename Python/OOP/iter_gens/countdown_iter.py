class countdown_iterator:
    def __init__(self, _count: int) -> None:
        self.count = _count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count != -1:
            num = self.count
            self.count -= 1
            return num
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
