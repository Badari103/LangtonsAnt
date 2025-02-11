from abc import ABC, abstractmethod

from direction.direction import Direction


class Colour(ABC):
    @abstractmethod
    def get_colour(self):
        pass

    @abstractmethod
    def flip_colour(self):
        pass

    @abstractmethod
    def rotate_direction(self, direction: Direction):
        pass

    @abstractmethod
    def print_colour(self):
        pass
