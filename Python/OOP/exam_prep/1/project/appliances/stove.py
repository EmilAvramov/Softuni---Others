from project.appliances.appliance import Appliance

class Stove(Appliance):
    def __init__(self) -> None:
        super().__init__(0.7)