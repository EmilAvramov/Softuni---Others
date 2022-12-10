from project.drink.tea import Tea
from project.drink.water import Water
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

inside_table = InsideTable(1, 4)
outside_table = OutsideTable(100, 6)

inside_table.reserve(4)
outside_table.reserve(6)

bread = Bread("Sourdough", 3.50)
cake = Cake("Cheesecake", 8.25)
tea = Tea("Green tea", 350, "Lipton")
water = Water("Mineral water", 500, "Borjomi")

inside_table.order_food(bread)
inside_table.order_food(cake)
inside_table.order_drink(tea)
outside_table.order_drink(water)

print(inside_table.get_bill())
inside_table1 = OutsideTable(50, 0)
