class Stack:
    def __init__(self, data=[]) -> None:
        self.data = data

    def push(self, item):
        self.data.append(item)

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[-1]

    def __repr__(self) -> str:
        return f"{' '.join(self.data)}"


data = [i for i in input().split(" ")]
reverse = Stack()

for i in range(len(data)):
    reverse.push(data.pop())

print(reverse)
