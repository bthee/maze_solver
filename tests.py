import unittest

from main import Maze, Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 12
        num_cols = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)


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


    def test_reset_cells_visited(self):
        win = Window(900, 700)
        maze = Maze(0, 0, 12, 16, 50, 50, win)
        maze._create_cells()
        maze._cells[5][5].visited = True 

        maze._reset_cells_visited()

        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited, "Not all cells are reset")


if __name__ == "__main__":
    unittest.main()

