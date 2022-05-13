class Shop:
    def __init__(self, _name: str, _items: list) -> None:
        self.name = _name
        self.items = _items

    def get_items_count(self):
        return len(self.items)
