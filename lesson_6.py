from random import randint
from tkinter import *
from turtle import color
 
# TODO: Add 2 more object at bottom left and right corners with different colors
# TODO: Add a Bot class to draw a grey rectangles and do it randomly in the middle of the game field
 
class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.draw()
 
    def moveto(self, x, y):
        self.x = x
        self.y = y
        self.draw()
 
    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5
    
    def draw(self):
        self.c.create_oval(self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2, fill=self.color)

class Bot:
    # x1, y1, x2, y2 = 100, 100, 300, 300
    bots = [4123]

    def __init__(self, c):
        self.x1, self.y1 = randint(100, 300), randint(100, 300)
        self.x2, self.y2 = self.x1+15, self.y1+15
        self.c = c

        # bots.append([(self.x1, self.y1), (self.x2, self.y2)])

        self.draw()
    
    def draw(self):
        self.c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='GREY')

root = Tk()
root.geometry("400x400")
canvas = Canvas(root, width=400, height=400)


p1 = Player(canvas, 25, 25, 20, "RED")
p2 = Player(canvas, 375, 25, 20, "BLUE")
p3 = Player(canvas, 25, 375, 20, "YELLOW")
p4 = Player(canvas, 375, 375, 20, "PINK")

bots = []
bots_coord = []


for _ in range(1000):
    bot = Bot(canvas)

    bots.append(bot)


canvas.pack()
root.mainloop()