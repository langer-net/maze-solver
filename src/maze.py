import random
import time
from typing import List, Tuple

from src.cell import Cell
from src.window import Window


class Maze:
    def __init__(self, x: int, y: int, num_cols: int, num_rows: int, cell_size_x: int, cell_size_y: int,
                 window: Window = None, seed: int = None) -> None:
        self._x = x
        self._y = y
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed is not None:
            random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(column_num=0, row_num=0)

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

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(column_num=0, row_num=0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(column_num=self._num_cols - 1, row_num=self._num_rows - 1)

    def _break_walls_r(self, column_num: int, row_num: int) -> None:
        self._cells[column_num][row_num].visited = True
        while True:
            possible_neighbors = self._get_unvisited_neighbors(column_num=column_num, row_num=row_num)
            # check for dead end and return if that is the case
            if len(possible_neighbors) == 0:
                self._draw_cell(column_num=column_num, row_num=row_num)
                return
            # randomly choose a direction to go
            direction_idx = random.randrange(len(possible_neighbors))
            *next_neighbor, direction = possible_neighbors[direction_idx]
            # remove walls between the current and the next cell
            self._remove_wall(current_column=column_num, current_row=row_num, next_column=next_neighbor[0],
                              next_row=next_neighbor[1], direction=direction)
            # recursively visit next cell
            self._break_walls_r(column_num=next_neighbor[0], row_num=next_neighbor[1])

    def _get_unvisited_neighbors(self, column_num: int, row_num: int) -> List[Tuple[int, int, str]]:
        unvisited_neighbors = []
        # list of directions: ((column_delta, row_delta, wall_removal_actions))
        directions = ((-1, 0, 'left'), (1, 0, 'right'), (0, -1, 'top'), (0, 1, 'bottom'))
        for column_delta, row_delta, direction in directions:
            new_column_num = column_num + column_delta
            new_row_num = row_num + row_delta
            if (0 <= new_column_num < self._num_cols and
                    0 <= new_row_num < self._num_rows and
                    not self._cells[new_column_num][new_row_num].visited):
                unvisited_neighbors.append((new_column_num, new_row_num, direction))
        return unvisited_neighbors

    def _remove_wall(self, current_column: int, current_row: int, next_column: int, next_row: int, direction: str):
        if direction == 'left':
            self._cells[current_column][current_row].has_left_wall = False
            self._cells[next_column][next_row].has_right_wall = False
        elif direction == 'right':
            self._cells[current_column][current_row].has_right_wall = False
            self._cells[next_column][next_row].has_left_wall = False
        elif direction == 'top':
            self._cells[current_column][current_row].has_top_wall = False
            self._cells[next_column][next_row].has_bottom_wall = False
        else:  # bottom
            self._cells[current_column][current_row].has_bottom_wall = False
            self._cells[next_column][next_row].has_top_wall = False
