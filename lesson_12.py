class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2


class Cyllinder(Circle):
    def __init__(self, r, h=0):
        self.h = h
        super().__init__(r)

    def get_area(self):
        return super().get_area() * 2 + (self.radius * 3.14 * 2) * self.h
        # return super().get_area()


p = Cyllinder(3, 5)
print(p.h)
print(p.r)
print(p.get_area())
