from typing import TypeVar, Tuple

from src.geometries import Line, Point
from src.window import Window

TCell = TypeVar("TCell", bound="Cell")


class Cell:
    def __init__(self, window: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._window = window
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self._window is None:
            return
        self._x1, self._x2 = x1, x2
        self._y1, self._y2 = y1, y2
        self._draw_wall(Point(x1, y1), Point(x1, y2), wall_exists=self.has_left_wall)
        self._draw_wall(Point(x2, y1), Point(x2, y2), wall_exists=self.has_right_wall)
        self._draw_wall(Point(x1, y1), Point(x2, y1), wall_exists=self.has_top_wall)
        self._draw_wall(Point(x1, y2), Point(x2, y2), wall_exists=self.has_bottom_wall)

    def draw_move(self, target_cell: TCell, undo: bool = False) -> None:
        if self._window is None:
            return
        fill_color = "gray" if undo else "red"
        x_middle, y_middle = self._get_middle_coordinates(self)
        target_x_middle, target_y_middle = self._get_middle_coordinates(target_cell)

        # moving left
        if self._x1 > target_cell._x1:
            self._draw_line_between_cells(self_point1=Point(x_middle, y_middle), self_point2=Point(self._x1, y_middle),
                                          target_point1=Point(target_x_middle, target_y_middle),
                                          target_point2=Point(target_cell._x2, target_y_middle), fill_color=fill_color)
        # moving right
        elif self._x1 < target_cell._x1:
            self._draw_line_between_cells(self_point1=Point(x_middle, y_middle), self_point2=Point(self._x2, y_middle),
                                          target_point1=Point(target_x_middle, target_y_middle),
                                          target_point2=Point(target_cell._x1, target_y_middle), fill_color=fill_color)
        # moving up
        elif self._y1 > target_cell._y1:
            self._draw_line_between_cells(self_point1=Point(x_middle, y_middle), self_point2=Point(x_middle, self._y1),
                                          target_point1=Point(target_x_middle, target_y_middle),
                                          target_point2=Point(target_x_middle, target_cell._y2), fill_color=fill_color)
        # moving down
        elif self._y1 < target_cell._y1:
            self._draw_line_between_cells(self_point1=Point(x_middle, y_middle), self_point2=Point(x_middle, self._y2),
                                          target_point1=Point(target_x_middle, target_y_middle),
                                          target_point2=Point(target_x_middle, target_cell._y1), fill_color=fill_color)

    def _draw_wall(self, start: Point, end: Point, wall_exists: bool) -> None:
        line = Line(start, end)
        if wall_exists:
            self._window.draw_line(line=line, fill_color="black")
        else:
            self._window.draw_line(line=line, fill_color="white")

    @staticmethod
    def _get_middle_coordinates(cell: TCell) -> Tuple[int, int]:
        return (cell._x1 + cell._x2) // 2, (cell._y1 + cell._y2) // 2

    def _draw_line_between_cells(self, self_point1: Point, self_point2: Point, target_point1: Point,
                                 target_point2: Point, fill_color: str) -> None:
        self._window.draw_line(line=Line(self_point1, self_point2), fill_color=fill_color)
        self._window.draw_line(line=Line(target_point1, target_point2), fill_color=fill_color)
