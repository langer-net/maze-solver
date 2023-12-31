from src.window import Window
from src.cell import Cell
from src.maze import Maze


def main() -> None:
    window = Window(width=800, height=600)

    maze = Maze(50, 50, 23, 16, 30, 30, window)

    window.wait_for_close()

if __name__ == "__main__":
    main()
