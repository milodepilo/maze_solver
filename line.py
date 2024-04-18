from point import Point

class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_colour,
            width = 2
        )
        canvas.pack()