from project.table.table import Table


class OutsideTable(Table):

    _MIN_NUMBER = 51
    _MAX_NUMBER = 100
    _TABLE_CLASS = 'Outside'

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(self.table_number, capacity)
