from direction.direction import Direction


class Backward(Direction):
    def get_direction(self):
        return self

    def rotate_clockwise(self):
        from direction.left import Left

        return Left()

    def rotate_counter_clockwise(self):
        from direction.right import Right

        return Right()

    def move(self, current_row, current_column):
        return current_row + 1, current_column

    def print_direction(self):
        return "Backward"
