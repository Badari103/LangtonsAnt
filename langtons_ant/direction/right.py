from direction.direction import Direction


class Right(Direction):
    def get_direction(self):
        return self

    def rotate_clockwise(self):
        from direction.backward import Backward

        return Backward()

    def rotate_counter_clockwise(self):
        from direction.forward import Forward

        return Forward()

    def move(self, current_row, current_column):
        return current_row, current_column + 1

    def print_direction(self):
        return "Right"
