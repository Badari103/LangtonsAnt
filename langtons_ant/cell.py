from ant.position import Position
from colour.white import White


class Cell:
    def __init__(self, row_number: int, column_number: int):
        self.position = Position(row_number, column_number)
        self.colour = White()

    def flip_colour(self):
        self.colour = self.colour.flip_colour()

    def get_position(self):
        return self.position.get_position()
    
    def print_colour(self):
        return self.colour.print_colour()
    
    def get_colour(self):
        return self.colour.get_colour()