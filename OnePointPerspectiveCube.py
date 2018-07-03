#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from itertools import cycle
from random import randint

COLORS = cycle(['red', 'blue', 'green', 'magenta', 'yellow'])
class PerspectiveCube:
    def __init__(self, canvas):
        self.canvas = canvas
        self.polygons = []
        color = next(COLORS)
        for _ in range(4):
            p = canvas.create_polygon(0,0,0,0,0,0, outline=color, fill='', width=4)
            self.canvas.tag_bind(p, "<B1-Motion>", self._on_clickndrag)
            self.polygons.append(p)
        self.canvas.tag_bind(self.polygons, "<B1-Motion>", self._on_clickndrag)
        self.update_screen(randint(50, 550), randint(50, 550)) #initial point

    def _on_clickndrag(self, event):
        self.update_screen(event.x, event.y)

    def update_screen(self, x, y):
        # A HORRIBLE MESS OF VARIABLES. DON'T LOOK. IT MIGHT BURN YOUR EYES.
        x1 = x-50
        y1 = y-50
        x2 = x+50
        y2 = y+50
        x3 = (300+x1)/2
        y3 = (300+y2)/2
        x4 = (300+x1+100)/2
        y4 = (300+y2)/2
        x5 = (300+x1)/2
        y5 = (300+y1)/2
        x6 = (300+x1)/2
        y6 = (300+y2)/2
        x7 = (300+x1+100)/2
        y7 = (300+y1)/2

        self.canvas.coords(self.polygons[0], x3, y3, x4, y4, x2, y2, x2 - 100, y2)
        self.canvas.coords(self.polygons[1], x5, y5, x6, y6, x2 - 100, y2, x1, y1)
        self.canvas.coords(self.polygons[2], x5, y5, x1, y1, x1+100, y1, x7, y7)
        self.canvas.coords(self.polygons[3], x2,y2,x1+100,y1,x7,y7, x4, y4)

class PerspectiveCanvas(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, bg='black', **kwargs)
        label = tk.Label(self, text = "Click and Drag to See the Shape",background='black',foreground='white')
        label.pack()
        self.canvas = tk.Canvas(self, width=600, height=600, bg='black')
        self.canvas.pack()
        btn = ttk.Button(self, text='add polygon', command=self.add)
        btn.place(relx=1, rely=0, anchor='ne')
        self.cubes = []

    def add(self):
        self.cubes.append(PerspectiveCube(self.canvas))

def main():
    root = tk.Tk()
    root.title("OnePointPerspectiveCube")
    root.configure(background='black')
    win = PerspectiveCanvas(root)
    win.pack()
    root.mainloop()

if __name__ == '__main__':
    main()

