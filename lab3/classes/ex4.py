import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)
        print(f"Distance between points: {distance}")
        return distance

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()


p1.move(7, 8)
p1.show()

p1.dist(p2)

