class Polygon:
    def __init__(self, square, rectangle, triangle):
        self.square = square
        self.rectangle = rectangle
        self.triangle = triangle

    def displayArea(self):
        print(self.square, "cm^2")
        print(self.rectangle, "cm^2")
        print(self.triangle, "cm^2")

class Area(Polygon):
    def __init__(self, square, rectangle, triangle, area):
        self.area = area

        Polygon.__init__(self, square, rectangle, triangle)

x = Area(6 * 6, 4 * 8, (0.5 * 4) * 5, "These are the area")
x.displayArea()