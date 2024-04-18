import time
from maze import Maze
import unittest

from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 7
        num_rows = 5
        m1 = Maze(50, 50, num_rows, num_cols, 100, 100, Window(1800, 720))
d
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows       
        ,
        )


    # def test_maze_create_cells_large(self):
    #     num_cols = 16
    #     num_rows = 12
    #     m1 = Maze(100, 100, num_rows, num_cols, 10, 10, Window(800, 600))
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )



if __name__ == "__main__":
    unittest.main()

