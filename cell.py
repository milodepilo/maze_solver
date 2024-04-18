from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, top_left: Point = None, bottom_right: Point = None, window: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self._win = window
        self.middle = self.calculate_middle()

    def draw(self):
        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            self._win.draw_line(Line(point_1, point_2),"black")
        
        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            self._win.draw_line(Line(point_1, point_2),"black")
        
        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            self._win.draw_line(Line(point_1, point_2),"black")
        
        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            self._win.draw_line(Line(point_1, point_2),"black")
        
    def calculate_middle(self) -> Point:
        x = (self._x1 + self._x2) / 2
        y = (self._y1 + self._y2) / 2
        return Point(x, y)
    
    def draw_move(self, to_cell: "Cell" , undo=False):
        if undo == False:
            self._win.draw_line(Line(self.middle, to_cell.middle), "red")
        else:
            self._win.draw_line(Line(self.middle, to_cell.middle), "gray")