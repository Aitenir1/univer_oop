import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi

    def perimeter(self):
        return 2 * self.r * math.pi

    def BelongsTo(self, x, y):
        return (self.x - x) ** 2 + (self.y - y) ** 2 <= self.r ** 2


c = Circle(0, 0, 3)

print(c.area())
print(c.perimeter())

print(c.BelongsTo(0, 0))
print(c.BelongsTo(1, 1))
print(c.BelongsTo(3, 3))
