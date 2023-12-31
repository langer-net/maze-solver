from src.cell import Cell
from src.window import Window


class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int,
                 window: Window) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[Cell(self._window) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(num_column=col, num_row=row)

    def _draw_cell(self, num_column: int, num_row: int) -> None:

        pass
