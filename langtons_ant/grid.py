from ant.ant import Ant
from cell import Cell


class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self.validate(rows, columns)
        self.grid = self.create_grid(rows, columns)

    def create_grid(self, rows: int, columns: int): 
        grid = [[Cell(row, column) for column in range(columns)] for row in range(rows)]
        return grid

    def validate(self, rows: int, columns: int):
        if rows < 3:
            raise ValueError("Rows must be greater than 2")
        if columns < 3:
            raise ValueError("Columns must be greater than 2")

    def validate_position(self, row: int, column: int):
        if row < 0 or row >= len(self.grid):
            raise IndexError("Row Limit Exceeded")
        if column < 0 or column >= len(self.grid[0]):
            raise IndexError("Column Limit Exceeded")

    def travel(self, ant: Ant, steps: int):
        for step in range(steps):
            current_row, current_column = ant.get_position()
            current_cell = self.grid[current_row][current_column]
            ant.rotate(current_cell.get_colour())
            ant.move(self.validate_position)
            current_cell.flip_colour()

    def print_grid(self):
        print("Grid:")
        for row in self.grid:
            for cell in row:
                print(cell.print_colour(), end=" ")
            print()
