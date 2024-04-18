from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
import time

def main():
    num_rows = 3
    num_cols = 3
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x =  100
    cell_size_y = 100
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    # maze._cells[1][1].draw_move(maze._cells[1][2]) 
    print(maze.solve())

    win.wait_for_close()
    

if __name__ == "__main__":
    main()