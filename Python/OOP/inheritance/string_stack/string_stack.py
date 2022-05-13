class Stack(str):
    def __init__(self) -> None:
        self.data = []

    def push(self, _element):
        self.data.append(_element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def __str__(self) -> str:
        result = "[" + ", ".join(sorted(self.data, reverse=True)) + "]"
        return result
