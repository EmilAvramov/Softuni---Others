from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self) -> None:
        super().__init__(1.5)
