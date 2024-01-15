import unittest

from main import Maze, Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells),num_cols,)
        self.assertEqual(len(m1._cells[0]),num_rows,)

    def test_maze_single_cell(self):
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m1._cells), 1)
        self.assertEqual(len(m1._cells[0]), 1)
        
    def test_break_entrance_and_exit(self):
        win = Window(900, 700)
        maze = Maze(0, 0, 12, 16, 50, 50, win)
        maze._break_entrance_and_exit()
        assert not maze._cells[0][0].has_top_wall, "Entrance wall is not broken"
        assert not maze._cells[-1][-1].has_bottom_wall, "Exit wall is not broken"


if __name__ == "__main__":
    unittest.main()

