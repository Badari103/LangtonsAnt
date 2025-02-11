from typing import Callable
from ant.position import Position
from colour.colour import Colour
from direction.forward import Forward

class Ant:
    def __init__(self, initial_row_number: int, initial_column_number: int):
        self.position = Position(initial_row_number, initial_column_number)
        self.direction = Forward()

    def rotate(self, colour: Colour):
        self.direction = colour.rotate_direction(self.direction)

    def move(self, validate_position: Callable[[int, int], None]):
        current_row, current_column = self.get_position()
        new_row, new_column = self.direction.move(current_row, current_column)
        self.position = Position(new_row, new_column)
        validate_position(new_row, new_column)

    def print_position(self):
        current_row, current_column = self.get_position()
        print(f"Ant position: row: {current_row}, column: {current_column}")

    def print_direction(self):
        print(f"Ant direction: {self.direction.print_direction()}")

    def get_position(self):
        return self.position.get_position()
