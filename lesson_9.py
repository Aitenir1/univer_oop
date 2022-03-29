import math
import numpy


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.NotaTriangle()

    def isosceles(self):
        print(
            f'Corner Alpha is {round(math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))), 1)}')
        print(
            f'Corner Beta is {round(math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))), 1)}')
        print(
            f'Corner Gamma is {round(math.degrees(math.acos((self.b ** 2 + self.a ** 2 - self.c ** 2) / (2 * self.b * self.a))), 1)}')
        if self.a == self.b and self.a != self.c:
            return True

        elif self.a == self.c and self.c != self.b:
            return True

        elif self.c == self.b and self.c != self.a:
            return True

        return False

    def right(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2:
            print(f'Гипотенуза is {self.c}')
            return True

        if self.b ** 2 + self.c ** 2 == self.a ** 2:
            print(f'Гипотенуза is {self.a}')
            return True

        if self.c ** 2 + self.a ** 2 == self.b ** 2:
            print(f'Гипотенуза is {self.b}')
            return True

        return False

    def Equilateral(self):
        if self.a == self.b == self.c:
            print(f'Area is {((3 ** (0.5)) / 4) * self.a ** 2}')
            return True

        return False

    def NotaTriangle(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            raise Exception('Unable to create such Triangle')


a, b, c = map(int, input().split())

t1 = Triangle(a, b, c)
print(t1.Equilateral())
print(t1.isosceles())
print(t1.right())
