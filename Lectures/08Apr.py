# Joshua Hamaker        04/08/2025
# Lecture notes - 04/08

## Classes & Objects
# public static void main(String[] args)-core


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, val):
        self.x = val
    def setY(self, val):
        self.y = val

p1 = Point(10, 15)
p2 = Point (2, 3)
p3 = Point(0, 0)

print(f"({p1.getX()}, {p1.getY()})")
print(f"({p2.getX()}, {p2.getY()})")
print(f"({p3.getX()}, {p3.getY()})")
p2.setY(1000)
print(f"({p2.getX()}, {p2.getY()})")