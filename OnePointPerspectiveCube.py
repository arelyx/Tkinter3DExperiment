#!/usr/bin/env python3

import tkinter as tk

class PerspectiveCube:
    def __init__(self, canvas):
        self.canvas = canvas
        self.polygons = []
        for _ in range(4):
            p = canvas.create_polygon(0,0,0,0,0,0, outline='red', fill='', width=4)
            self.canvas.tag_bind(p, "<B1-Motion>", self._on_clickndrag)
            self.polygons.append(p)
        self.canvas.tag_bind(self.polygons, "<B1-Motion>", self._on_clickndrag)
        self.update_screen(200, 200) #initial point

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

def main():
    root = tk.Tk()
    root.title("OnePointPerspectiveCube")
    root.configure(background='black')
    label = tk.Label(text = "Click and Drag to See the Shape",background='black',foreground='white')
    label.pack()
    canvas = tk.Canvas(width=600, height=600, bg='black')
    canvas.pack()
    x = PerspectiveCube(canvas)
    root.mainloop()

if __name__ == '__main__':
    main()

