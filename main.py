from window import Window
from line import Line
from point import Point
from cell import Cell
import time

def main():
    points = [
        Point(100, 100),
        Point(100, 300),
        Point(200, 300),
        Point(200, 200)
    ]
    window = Window(800, 600)
        
    num_cells_x = 8  # Number of cells horizontally
    num_cells_y = 10   # Number of cells vertically
    cell_width = 800 // num_cells_x
    cell_height = 600 // num_cells_y

    cells:list[Cell] = []
    
    for i in range(num_cells_y):
        for j in range(num_cells_x):
            top_left = Point(j * cell_width, i * cell_height)
            bottom_right = Point((j + 1) * cell_width, (i + 1) * cell_height)
            cell = Cell(top_left, bottom_right, window)
            cells.append(cell)

    cells[0].draw_move(cells[1])
    window.wait_for_close()

if __name__ == "__main__":
    main()