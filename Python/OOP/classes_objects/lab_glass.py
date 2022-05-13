class Glass:
    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, _ml: int):
        if Glass.capacity >= _ml:
            self.content += _ml
            Glass.capacity -= _ml
            return f"Glass filled with {_ml} ml"
        else:
            return f"Cannot add {_ml} ml"

    def empty(self):
        self.content = 0
        Glass.capacity = 250
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
