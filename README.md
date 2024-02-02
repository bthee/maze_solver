# MAZE SOLVER
This application visually generates and solves a maze.

## INSTALLATION


## STRUCTURE
The program is based on the following classes:

Window: Represents the main application window using Tkinter.\
Point and Line: These classes are used to draw the outline of the maze. A Point is a 2D point with x and y coordinates, a Line is a line segment between two points.\
Cell: Represents a cell in the maze. Each cell knows whether it has walls on its sides.\
Maze: Represents the overall maze structure. It can generate a new maze and solve it.\
APPROACH\
The Maze class generates a maze randomly and solves it using depth-first search algorithm.

## HOW TO USE
Run the main.py file and it will create a maze utilizing the settings provided. The maze will then solve itself.

## CUSTOMIZATION
You can customize the size of the maze (rows and columns), the size of the cells, and the starting point of the maze generation by modifying the corresponding parameters in the main function.