from abc import ABC
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_bill = 0
        for food in self.food_orders:
            total_bill += food.price
        for drink in self.drink_orders:
            total_bill += drink.price
        return total_bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return (
                f"Table: {self.table_number}\n"
                f"Type: {self.__class__.__name__}\n"
                f"Capacity: {self.capacity}"
            )
