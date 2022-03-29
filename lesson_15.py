import tkinter as tk



class Field:
    def __init__(self, c: tk.Canvas, n, m, width, height, walls=False):
        '''
        c - canvas instance
        n - number of rows
        m - number of columns
        width - width of game field in pixels
        height - width of game field in pixels
        walls - if True matrix should have 0's surrounded by 1's (walls)
        example
        1 1 1 1
        1 0 0 1
        1 1 1 1
        '''
        self.c = c
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.walls = walls

        matrix = [[1 if walls else 0 for _ in range(m)]]

        for i in range(n-2):
            row = [1 if walls else 0]
            for j in range(m-2):
                row.append(0)
            row.append(1 if walls else 0)
            matrix.append(row)
        
        matrix.append([1 if walls else 0 for _ in range(m)])
    
        self.matrix= matrix

        self.block_h = height / n
        self.block_w = width / m
    
    def draw(self):
        y = 0

        for i in self.matrix:
            x = 0

            for j in i:
                self.c.create_rectangle(x, y, x+self.block_w, y+self.block_h, fill=('BLACK' if j else 'WHITE'), outline='GREY')
                x += self.block_w
            
            y += self.block_h



root = tk.Tk()
root.geometry('500x500')

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

f = Field(canvas, 20, 20, 500, 500, True)


f.draw()
root.mainloop()