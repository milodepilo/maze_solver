import random
from turtle import pos
from cell import Cell
from point import Point
from window import Window
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit_walls()
        self._break_walls_r(0, 0)
 
        self._reset_cells_visited()

    def _create_cells(self):
    # Populate the self._cells list with columns of Cell objects
        self._cells: list[list[Cell]] = []
        for i in range(self.num_cols):
            column: list[Cell] = []
            for j in range(self.num_rows):
                # Create each cell but do not calculate position yet
                cell = Cell(self._win)  # We'll position it in _draw_cell
                column.append(cell)
            self._cells.append(column)
        
   # Now, draw each cell at its correct position
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        





    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        time.sleep(0.1)
        self._win.redraw()

    def _break_entrance_and_exit_walls(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance.has_bottom_wall = False
        entrance.has_left_wall = False
        entrance.has_right_wall = False
        entrance.has_top_wall = False
        self._draw_cell(0,0)
        exit.has_bottom_wall = False
        exit.has_left_wall = False
        exit.has_right_wall = False
        exit.has_top_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i < self.num_cols  - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self._cells[i][j -1].visited:
                possible_directions.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(len(possible_directions))
            next_cell = possible_directions[direction]
            
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):

        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        print(f"Attempting to solve from ({i}, {j})")
        time.sleep(0.075)
        self._animate()

        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.num_rows - 1][self.num_cols - 1]:
            return True
        #left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i - 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        #right
        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i + 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        #down
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j - 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        #up
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j + 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False



