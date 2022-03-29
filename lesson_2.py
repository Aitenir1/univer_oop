class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 20
    
    def moveto(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, x, y):
        return ((x - self.x) ** 2 + (y - self.y) ** 2) ** 0.5


azamat = Player(0, 0, 30)

print(azamat.distance(5, 5))