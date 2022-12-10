from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:
    def __init__(self, name: str):
        if name.isspace() or name == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        else:
            raise Exception("Invalid food type!")

        for f in self.food_menu:
            if f.name == food.name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(
        self, drink_type: str, name: str, portion: float, brand: str
    ):
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        else:
            raise Exception("Invalid drink type!")

        for d in self.drinks_menu:
            if d.name == drink.name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        else:
            raise Exception("Invalid table type!")

        for t in self.tables_repository:
            if t.table_number == table.table_number:
                raise Exception(
                    f"Table {table_number} is already in the bakery!"
                )

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
                break
        if not table:
            return f"Could not find table {table_number}"

        ordered_food = []
        not_in_menu = []
        for food_name in food_names:
            found = False
            for food in self.food_menu:
                if food.name == food_name:
                    found = True
                    ordered_food.append(food)
                    table.order_food(food)
                    break
            if not found:
                not_in_menu.append(food_name)

        result = [f"Table {table_number} ordered:"]
        for food in ordered_food:
            result.append(
                f" - {food.name}: {food.portion}g - {food.price:.2f}lv"
            )
        result.append(f"{self.name} does not have in the menu:")
        for food_name in not_in_menu:
            result.append(f" - {food_name}")

        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
                break
        if not table:
            return f"Could not find table {table_number}"

        not_found_drinks = []
        ordered_drinks = []
        for drink in drinks:
            found = False
            for d in self.drinks_menu:
                if d.name == drink:
                    table.order_drink(d)
                    ordered_drinks.append(d)
                    found = True
                    break
            if not found:
                not_found_drinks.append(drink)

        result = ["Table {table_number} ordered:"]
        for drink in ordered_drinks:
            result.append(str(drink))
        if not_found_drinks:
            result.append(f"{self.name} does not have in the menu:")
            for drink in not_found_drinks:
                result.append(drink)

        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
                break
        if not table:
            return f"Could not find table {table_number}"

        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        return f"Table: {table_number}\nBill: {bill:.2f}lv"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
