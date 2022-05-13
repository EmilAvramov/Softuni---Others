class Car:
    def __init__(self, _name: str, _model: str, _engine: str) -> None:
        self.name = _name
        self.model = _model
        self.engine = _engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"
