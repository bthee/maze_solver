from tkinter import Tk, BOTH, Canvas
import time
import random

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height, bg="white")
        self.__canvas.pack(fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close) 

    def redraw(self):
         self.__root.update_idletasks()
         self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _x1, _y1, _x2, _y2, _win=None):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
        self.visited = False

    def draw(self):
        wall_color = "black"
        no_wall_color = "white"

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(left_wall, wall_color if self.has_left_wall else no_wall_color)

        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(right_wall, wall_color if self.has_right_wall else no_wall_color)

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(top_wall, wall_color if self.has_top_wall else no_wall_color)

        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(bottom_wall, wall_color if self.has_bottom_wall else no_wall_color)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"

        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2

        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2

        move_line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(move_line, color)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1 + 50
        self.y1 = y1 + 50
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = [[Cell(True, True, True, True,
                     self.x1 + i * self.cell_size_x,
                     self.y1 + j * self.cell_size_y,
                     self.x1 + (i+1) * self.cell_size_x,
                     self.y1 + (j+1) * self.cell_size_y,
                     self.win)
                for j in range(self.num_rows)] 
               for i in range(self.num_cols)]
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []

            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i < self.num_cols-1 and not self._cells[i+1][j].visited: 
                to_visit.append((i+1, j))
            if not to_visit:
                return
            
            next_i, next_j = random.choice(to_visit)

            if (0 < next_i < self.num_rows-1) and (0 < next_j < self.num_cols-1):
                if next_i > i:
                    current_cell.has_bottom_wall = False
                    self._cells[next_i][next_j].has_top_wall = False
                elif next_i < i:
                    current_cell.has_top_wall = False
                    self._cells[next_i][next_j].has_bottom_wall = False
                elif next_j > j:
                    current_cell.has_right_wall = False
                    self._cells[next_i][next_j].has_left_wall = False
                elif next_j < j:
                    current_cell.has_left_wall = False
                    self._cells[next_i][next_j].has_right_wall = False

            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)
            self._break_walls_r(next_i, next_j)



if __name__ == "__main__":
    win = Window(900, 700)
    maze = Maze(0, 0, 12, 16, 50, 50, win, seed=0)
    maze._create_cells()

    for i in range(16):
        for j in range(12):
            maze._draw_cell(i, j)
    
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)

    win.wait_for_close()
