from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self) -> None:
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        food = None
        if type_delicacy == "Gingerbread":
            food = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            food = Stolen(name, price)
        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for food in self.delicacies:
            if food.name == name:
                raise Exception(f"{name} already exists!")

        if food:
            self.delicacies.append(food)
            return (
                f"Added delicacy {name} - {type_delicacy} to the pastry shop."
            )
        else:
            raise Exception("Check this")

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = None
        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if booth:
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."
        else:
            raise Exception("Check this")

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                for food in self.delicacies:
                    if food.name == delicacy_name:
                        booth.delicacy_orders.append(food)
                        return f"Booth {booth_number} ordered {delicacy_name}."
                raise Exception(f"No {delicacy_name} in the pastry shop!")
        raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int):
        bill = 0
        for booth in self.booths:
            if booth.booth_number == booth_number:
                bill += booth.price_for_reservation
                for order in booth.delicacy_orders:
                    bill += order.price
                booth.delicacy_orders = []
                booth.is_reserved = False
                booth.price_for_reservation = 0
        self.income += bill
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
