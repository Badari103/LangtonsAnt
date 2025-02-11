from abc import ABC, abstractmethod


class Direction(ABC):
    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def rotate_clockwise(self):
        pass

    @abstractmethod
    def rotate_counter_clockwise(self):
        pass

    @abstractmethod
    def move(self, current_row, current_column):
        pass

    @abstractmethod
    def print_direction(self):
        pass
