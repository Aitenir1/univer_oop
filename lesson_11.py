class Rectanble:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        self.areap = self.width * self.length
        return self.areap

    def perimeter(self):
        self.perimeterp = 2 * (self.width + self.length)
        return self.perimeterp
    
    def display(self):
        print(f'Area is {self.areap}')
        print(f'Perimeter is {self.perimeterp}')

class Parallelepiped(Rectanble):
    def __init__(self, height, width, length):
        self.height = height
        super().__init__(width, length)
    
    def volume(self):
        self.volumep = self.height * self.width * self.length
        return self.volumep
    
    def display(self):
        print(f'Volume is {self.volumep}')
        return super().display()

p3 = Parallelepiped(4, 3, 5)
p3.area()
p3.perimeter()
p3.volume()

p3.display()