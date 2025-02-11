from colour.colour import Colour


class White(Colour):
    def get_colour(self):
        return self

    def flip_colour(self):
        from colour.black import Black

        return Black()

    def rotate_direction(self, direction):
        return direction.rotate_clockwise()

    def print_colour(self):
        colour_value = "0"
        return colour_value
