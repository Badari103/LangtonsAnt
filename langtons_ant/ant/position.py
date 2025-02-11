class Position:
    row_number: int
    column_number: int

    def __init__(self, row_number: int, column_number: int):
        self.row_number = row_number
        self.column_number = column_number

    def get_position(self):
        return self.row_number, self.column_number