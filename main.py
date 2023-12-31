from src.maze import Maze
from src.window import Window


def main() -> None:
    window = Window(width=800, height=600)
    maze = Maze(x=50, y=50, num_cols=23, num_rows=16, cell_size_x=30, cell_size_y=30, window=window)
    maze.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()
