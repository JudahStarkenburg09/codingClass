from tkinter import *
import tkinter as tk
import random
import os
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry('800x900')
window.title("Time Teller App")
window.config(bg='gray')
window.resizable(False, False)

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

def findAllOutcomes():
    # make a grid?
    for vertical in range(3):
        # increase vertical direction to make 3x3 grid
        for horizontal in range(3):
            # increase horizontal direction to make 3x3 grid
            gridPosx, gridPosy = (160, 190) #GRID POSITION
            distanceBetweenCellsX, distanceBetweenCellsY = (250, 250) #DISTANCE BETWEEN GRID CELLS
            
            x = horizontal * distanceBetweenCellsX + gridPosx
            y = vertical * distanceBetweenCellsY + gridPosy
            canvas.create_image(x, y, image=photo)
            
    canvas.create_rectangle(295, 350, 505, 540, fill='gray', outline='gray')

def insertText():
    for v in range(3):
        for h in range(3)
            Y, m, d, H = random.randrange(1,70), random.randrange(1,11), random.randrange(1,28), random.randrange(1,23)


canvas = Canvas(window, width=5000, height=5000)
canvas.config(bg='gray')
canvas.pack()

# Open and resize the image
image = Image.open('dial.png')
resized_image = image.resize((330, 196))

# Create the PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)


findAllOutcomes()
resized_image2 = image.resize((450,267))
photo2 = ImageTk.PhotoImage(resized_image2)
canvas.create_image(415, 440, image=photo2)

window.mainloop()
