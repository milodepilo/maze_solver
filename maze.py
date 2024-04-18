from cell import Cell
from point import Point
from window import Window
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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
    # Populate the self._cells list with columns of Cell objects
        self._cells = []
        for j in range(self.num_cols):
            column = []
            for i in range(self.num_rows):
                # Create each cell but do not calculate position yet
                cell = Cell(None, None, self._win)  # We'll position it in _draw_cell
                column.append(cell)
            self._cells.append(column)

    # Now, draw each cell at its correct position
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Calculate the top-left and bottom-right points based on the cell's position
        x = self.x1 + j * self.cell_size_x
        y = self.y1 + i * self.cell_size_y
        top_left = Point(x, y)
        bottom_right = Point(x + self.cell_size_x, y + self.cell_size_y)

        # Update the cell's position
        cell = self._cells[j][i]
        cell._x1, cell._y1 = top_left.x, top_left.y
        cell._x2, cell._y2 = bottom_right.x, bottom_right.y

        # Assume Cell has a method to draw itself properly
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()

            

