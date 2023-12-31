import unittest

from src.maze import Maze


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.num_cols = 12
        self.num_rows = 10
        self.maze = Maze(x=0, y=0, num_cols=self.num_cols, num_rows=self.num_rows, cell_size_x=10, cell_size_y=10)

    def test_maze_create_cells(self) -> None:
        self.assertEqual(
            len(self.maze._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.maze._cells[0]),
            self.num_rows,
        )

    def test_maze_break_entrance_and_exit(self) -> None:
        self.assertEqual(self.maze._cells[0][0].has_top_wall, False)
        self.assertEqual(self.maze._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall, False)

    def test_reset_cells_visited(self) -> None:
        cells = [cell for column in self.maze._cells for cell in column]
        for cell in cells:
            self.assertEqual(cell.visited, False)


if __name__ == '__main__':
    unittest.main()
