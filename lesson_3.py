import re

class Person:

    def __init__(self, x=1, y=1):
        pass

    def set_size(self, size):
        if size <= 0:
            raise Exception('Value should be greater than 0')
        self.size = size
    
    def set_name(self, name):
        if not name.isascii() or len(name) not in range(4, 20) or name[0].upper() != name[0]:
            raise Exception('Name error. Follow rules.')

        for i in name:
            if i.isdigit():
                raise Exception('Name error. Follow rules.')

        self.name = name

b = Person()
b.set_size(12)
b.set_name('Flock')

print(b.size)
print(b.name)