class Equipment:
    id = 1

    def __init__(self, _name: str) -> None:
        self.name = _name
        self.id = Equipment.id
        Equipment.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
