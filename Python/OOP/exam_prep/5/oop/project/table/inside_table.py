from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int) -> None:
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.table_number

    @table_number.setter
    def table_number(self, value: int):
        if value < 1 or value > 50:
            raise ValueError(
                "Inside table's number must be between 1 and 50 inclusive!"
            )
        self.table_number = value
