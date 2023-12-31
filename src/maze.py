import time

from src.cell import Cell
from src.window import Window


class Maze:
    def __init__(self, x: int, y: int, num_cols: int, num_rows: int, cell_size_x: int, cell_size_y: int,
                 window: Window = None) -> None:
        self._x = x
        self._y = y
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[Cell(self._window) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for column_num in range(self._num_cols):
            for row_num in range(self._num_rows):
                self._draw_cell(column_num=column_num, row_num=row_num)

    def _draw_cell(self, column_num: int, row_num: int) -> None:
        x1 = self._x + (self._cell_size_x * column_num)
        x2 = x1 + self._cell_size_x
        y1 = self._y + (self._cell_size_y * row_num)
        y2 = y1 + self._cell_size_y
        self._cells[column_num][row_num].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.001)
