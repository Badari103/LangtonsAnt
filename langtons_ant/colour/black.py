from colour.colour import Colour


class Black(Colour):
    def get_colour(self):
        return self

    def flip_colour(self):
        from colour.white import White

        return White()

    def rotate_direction(self, direction):
        return direction.rotate_counter_clockwise()
    
    def print_colour(self):
        colour_value = "1"
        return colour_value
