from project.appliances.appliance import Appliance

class Laptop(Appliance):
    def __init__(self) -> None:
        super().__init__(1)