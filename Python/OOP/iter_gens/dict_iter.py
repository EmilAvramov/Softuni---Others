class dictionary_iter:
    def __init__(self, _dict: dict) -> None:
        self.dictionary = _dict
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != len(self.dictionary):
            for index, pair in enumerate(self.dictionary):
                if index == self.index:
                    self.index += 1
                    return (pair, self.dictionary[pair])
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
