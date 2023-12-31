from src.window import Window
from src.cell import Cell
from src.maze import Maze


def main() -> None:
    window = Window(width=800, height=600)

    c1 = Cell(window)
    c1.has_right_wall = False
    c1.draw(x1=50, y1=50, x2=100, y2=100)

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(x1=100, y1=50, x2=150, y2=100)

    c1.draw_move(c2)

    c3 = Cell(window)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(x1=100, y1=100, x2=150, y2=150)

    c2.draw_move(c3)

    c4 = Cell(window)
    c4.has_left_wall = False
    c4.draw(x1=150, y1=100, x2=200, y2=150)

    c3.draw_move(c4, undo=True)

    window.wait_for_close()

    maze = Maze(50, 50, 10, 20, 50, 50, window)


if __name__ == "__main__":
    main()
