from tkinter import Tk, BOTH, Canvas

from src.geometries import Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg="white", width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=True)
        self._running = False

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(canvas=self._canvas, fill_color=fill_color)

    def wait_for_close(self) -> None:
        self._running = True
        while self._running:
            self.redraw()

    def close(self) -> None:
        self._running = False
