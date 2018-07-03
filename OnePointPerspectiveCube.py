#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from itertools import cycle
from random import randint

BOX_SIZE = 35
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
        self.update_screen(
            randint(BOX_SIZE, canvas.winfo_width()),
            randint(BOX_SIZE, canvas.winfo_height())) #initial point

    def _on_clickndrag(self, event):
        self.update_screen(event.x, event.y)

    def update_screen(self, x=None, y=None):
        # A HORRIBLE MESS OF VARIABLES. DON'T LOOK. IT MIGHT BURN YOUR EYES.
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        half_width = self.canvas.winfo_width() / 2
        half_height = self.canvas.winfo_height() / 2
        x1 = self.x-BOX_SIZE
        y1 = self.y-BOX_SIZE
        x2 = self.x+BOX_SIZE
        y2 = self.y+BOX_SIZE
        x3 = (half_width+x1)/2
        y3 = (half_height+y2)/2
        x4 = (half_width+x1+BOX_SIZE*2)/2
        y4 = (half_height+y2)/2
        x5 = (half_width+x1)/2
        y5 = (half_height+y1)/2
        x6 = (half_width+x1)/2
        y6 = (half_height+y2)/2
        x7 = (half_width+x1+BOX_SIZE*2)/2
        y7 = (half_height+y1)/2

        self.canvas.coords(self.polygons[0], x3, y3, x4, y4, x2, y2, x2 - BOX_SIZE*2, y2)
        self.canvas.coords(self.polygons[1], x5, y5, x6, y6, x2 - BOX_SIZE*2, y2, x1, y1)
        self.canvas.coords(self.polygons[2], x5, y5, x1, y1, x1+BOX_SIZE*2, y1, x7, y7)
        self.canvas.coords(self.polygons[3], x2,y2,x1+BOX_SIZE*2,y1,x7,y7, x4, y4)

class PerspectiveCanvas(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, bg='black', **kwargs)
        label = tk.Label(self, text = "Click and Drag to See the Shape",background='black',foreground='white')
        label.pack()
        self.canvas = tk.Canvas(self, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.update_all)
        btn = ttk.Button(self, text='add polygon', command=self.add)
        btn.place(relx=1, rely=0, anchor='ne')
        self.cubes = []

    def add(self):
        self.cubes.append(PerspectiveCube(self.canvas))

    def update_all(self, event):
        for cube in self.cubes:
            cube.update_screen()

def main():
    root = tk.Tk()
    root.title("OnePointPerspectiveCube")
    root.configure(background='black')
    root.geometry('600x600')
    win = PerspectiveCanvas(root)
    win.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()

