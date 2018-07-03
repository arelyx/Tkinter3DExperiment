from tkinter import *

def shape(event):
    global line_one, line_two, line_three, line_four, polygon_bottom, polygon_top, polygon_left, polygon_right
    canvas.delete(line_one, line_two, line_three, line_four,polygon_bottom, polygon_top, polygon_left, polygon_right)

    # A HORRIBLE MESS OF VARIABLES. DON'T LOOK. IT MIGHT BURN YOUR EYES.
    x = event.x
    y = event.y
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


    # UNCOMMENT FOR A FREE COOKIE!
    # line_one = canvas.create_line(300,300,x1,y1, fill='white')
    # line_two = canvas.create_line(300,300,x1+100,y1, fill='white')
    # line_three = canvas.create_line(300,300,x2-100,y2, fill='white')
    # line_four = canvas.create_line(300,300,x2,y2, fill='white')

    polygon_bottom = canvas.create_polygon(x3, y3, x4, y4, x2, y2, x2 - 100, y2, outline='red', fill='', width=4)
    polygon_left = canvas.create_polygon(x5, y5, x6, y6, x2 - 100, y2, x1, y1, outline='red', fill='', width=4)
    polygon_top = canvas.create_polygon(x5, y5, x1, y1, x1+100, y1, x7, y7, outline='red', fill='', width=4)
    polygon_right= canvas.create_polygon(x2,y2,x1+100,y1,x7,y7, x4, y4, outline='red', fill='', width=4)


tk = Tk()
tk.title("OnePointPerspectiveCube")
tk.configure(background='black')
label = Label(text = "Click and Drag to See the Shape",background='black',foreground='white')
label.pack()
canvas = Canvas(width=600, height=600, bg='black')
canvas.pack()

line_one = canvas.create_line(0,0,0,0)
line_two = canvas.create_line(0,0,0,0)
line_three = canvas.create_line(0,0,0,0)
line_four = canvas.create_line(0,0,0,0)
polygon_bottom = canvas.create_polygon(0,0,0,0,0,0)
polygon_top = canvas.create_polygon(0,0,0,0,0,0)
polygon_left = canvas.create_polygon(0,0,0,0,0,0)
polygon_right = canvas.create_polygon(0,0,0,0,0,0)

canvas.bind("<B1-Motion>",shape)

tk.mainloop()
