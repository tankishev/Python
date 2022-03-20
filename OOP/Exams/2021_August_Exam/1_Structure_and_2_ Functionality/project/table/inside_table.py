from project.table.table import Table


class InsideTable(Table):

    _MIN_NUMBER = 1
    _MAX_NUMBER = 50
    _TABLE_CLASS = 'Inside'

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(self.table_number, capacity)
