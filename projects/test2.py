from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.geometry('800x800')
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("donut.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
root.mainloop()