from ant.ant import Ant
from grid import Grid


def main():
    try:
        print("Enter row: ")
        rows = int(input())
        print("Enter column: ")
        columns = int(input())
        print("Enter number of steps: ")
        steps = int(input())
        print("Enter initial row position for ant: ")
        initial_ant_row_position = int(input())
        print("Enter initial column position for ant: ")
        initial_ant_column_position = int(input())
        grid = Grid(rows, columns)
        ant = Ant(initial_ant_row_position, initial_ant_column_position)
        grid.travel(ant, steps)
    except IndexError as e:
        print(f"Error: {e}")
        return
    finally:
        grid.print_grid()
        ant.print_position()
        ant.print_direction()


if __name__ == "__main__":
    main()
