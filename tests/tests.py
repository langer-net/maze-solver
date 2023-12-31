import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(x=0, y=0, num_cols=num_cols, num_rows=num_rows, cell_size_x=10, cell_size_y=10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 26
        m1 = Maze(x=0, y=0, num_cols=num_cols, num_rows=num_rows, cell_size_x=10, cell_size_y=10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


if __name__ == '__main__':
    unittest.main()