from tkinter import *
from time import sleep
from random import randint
 
class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(self.x - self.size / 2,
        self.y - self.size / 2,
        self.x + self.size / 2,
        self.y + self.size / 2, 
        fill=self.color)
 
    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()
 
    def draw(self):
 
        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)
 
        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(100, self.draw)
 
 
    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5


class Hero(Player):
    # If boostrate is 2, then speed of the Hero is larger than the others 2 times

    def __init__(self, boostrate, stamina, c, x, y, size, color="RED"):
        self.boostrate = boostrate
        self.stamina = stamina
        super().__init__(c, x, y, size, color)

    def draw(self):
        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)
 
        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(int(100 / self.boostrate), self.draw)

root = Tk()
root.geometry("400x400")
c = Canvas(root, width=400, height=400)
c.pack()
 
p1 = Player(c, 25, 25, 20, "GREEN")
p2 = Player(c, 375, 25, 20, "RED")
p3 = Hero(10, 5, c, 25, 375, 20, "BLACK") 

p1.moveto(200, 200)
p2.moveto(200, 200)
p3.moveto(200, 200)
root.mainloop()
# c.create_oval(p.x + 5,p.y + 5,p.x+p.size + 5,p.y+p.size + 5)