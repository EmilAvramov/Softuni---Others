from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass
