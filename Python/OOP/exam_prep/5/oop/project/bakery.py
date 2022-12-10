from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.food_menu: list = []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income = 0
        self.valid_foods: list = ["Bread", "Cake"]
        self.valid_drinks: list = ["Tea", "Water"]
        self.valid_tables: list = ["InsideTable", "OutsideTable"]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.name = value

    def get_food(self, food_name: str):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return False

    def get_drink(self, drink_name: str):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return False

    def get_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return False

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in self.valid_foods:
            if self.get_food(name) is False:
                if food_type == "Bread":
                    food = Bread(name, price)
                elif food_type == "Cake":
                    food = Cake(name, price)
                self.food_menu.append(food)
                return f"Added {name} ({food_type}) to the food menu"
            raise Exception(f"{food_type} {name} is already in the menu!")

    def add_drink(
        self, drink_type: str, name: str, portion: float, brand: str
    ):
        if drink_type in self.valid_drinks:
            if self.get_drink(name) is False:
                if drink_type == "Tea":
                    drink = Tea(name, portion, brand)
                elif drink_type == "Water":
                    drink = Water(name, portion, brand)
                self.drinks_menu.append(drink)
                return f"Added {name} ({brand}) to the drink menu"
            raise Exception(f"{drink_type} {name} is already in the menu!")

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in self.valid_tables:
            if self.get_table(table_number is False):
                if table_type == "InsideTable":
                    table = InsideTable(table_number, capacity)
                elif table_type == "OutsideTable":
                    table = OutsideTable(table_number, capacity)
                self.tables_repository.append(table)
                return f"Added table number {table_number} in the bakery"
            raise Exception(f"Table {table_number} is already in the bakery!")

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved is False and table.number_of_people >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self.get_table(table_number)
        available = []
        unavailable = []
        result = []
        if table:
            for food_name in food_names:
                food = self.get_food(food_name)
                if food:
                    available.append(str(food))
                    table.order_food(food)
                else:
                    unavailable.append(food_name)
            result.append(f"Table {table_number} ordered:")
            result.append(x for x in available)
            result.append(f"{self.name} does not have in the menu:")
            result.append(x for x in unavailable)
            return '\n'.join(result)
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drink_names: str):
        table = self.get_table(table_number)
        available = []
        unavailable = []
        result = []
        if table:
            for drink_name in drink_names:
                drink = self.get_drink(drink_name)
                if drink:
                    available.append(str(drink))
                    table.order_drink(drink)
                else:
                    unavailable.append(drink_name)
            result.append(f"Table {table_number} ordered:")
            result.append(x for x in available)
            result.append(f"{self.name} does not have in the menu:")
            result.append(x for x in unavailable)
            return f"{'\n'.join(result)}"
        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        table = self.get_table(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table_number}\nBill: {bill}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())
        return f"{'\n'.join(result)}"

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
