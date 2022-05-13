class Employee:
    def __init__(
        self, _id: int, _first_name: str, _last_name: str, _salary: int
    ) -> None:
        self.id = _id
        self.first_name = _first_name
        self.last_name = _last_name
        self.salary = _salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, _amount: int):
        self.salary += _amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
