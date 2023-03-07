from tkinter import *
import random
root = Tk()
root.geometry('300x400')

canvas = Canvas(root, width=200, height=200)
canvas.pack()


import random

positions = [[10, 50, 60, 100], [100, 50, 150, 100]]
rectangle1choice = random.choice(positions)
positions.remove(rectangle1choice)  # remove the position of rectangle1 from the list
rectangle2choice = random.choice(positions)


pos1x1, pos1y1, pos1x2, pos1y2 = rectangle1choice
pos2x1, pos2y1, pos2x2, pos2y2 = rectangle2choice


# Draw a rectangle on the canvas
rectangle1 = canvas.create_rectangle(pos1x1, pos1y1, pos1x2, pos1y2, fill="red")

# Draw a rectangle on the canvas
rectangle2 = canvas.create_rectangle(pos2x1, pos2y1, pos2x2, pos2y2, fill="blue")

def on_click(event):
    # Check if the mouse click was inside the red
    if (event.x >= pos1x1 and event.y >= pos1y1 and event.x <= pos1x2 and event.y <= pos1y2):
        print("Hello")
    # Check if the mouse click was inside the blue
    elif (event.x >= pos2x1 and event.y >= pos2y1 and event.x <= pos2x2 and event.y <= pos2y2):
        print("Hello")

# Bind the click event to the rectangle
canvas.tag_bind(rectangle1, "<Button-1>", on_click)
canvas.tag_bind(rectangle2, "<Button-1>", on_click)

root.mainloop()
