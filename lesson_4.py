class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.length
    
    def area(self):
        self.area = self.width * self.length
    
    def display(self):
        return self.area, self.perimeter
    
n, m = map(int, input().split())
a = Rectangle(n, m)
a.perimeter()
a.area()
print(a.display())