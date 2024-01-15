from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height)
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



win = Window(800, 600)
win.wait_for_close()