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


def generate_percentages():
    percentages = [random.uniform(0, 100) for _ in range(9)]
    total = sum(percentages)
    # Normalize the percentages so that they add up to 100
    percentages = [int(p/total*100) for p in percentages]
    # Sort the percentages in decreasing order
    percentages.sort(reverse=True)
    return percentages

def findAllOutcomes():
    percentages = generate_percentages()
    texts = [str(p)+'%' for p in percentages]
    # move the largest number to the middle of the list
    texts = texts[1:5] + [texts[0]] + texts[5:]
    # Make a grid?
    gridPosx, gridPosy = (160, 190) #GRID POSITION
    distanceBetweenCellsX, distanceBetweenCellsY = (250, 250) #DISTANCE BETWEEN GRID CELLS
    for vertical in range(3):
        # Increase vertical direction to make 3x3 grid
        for horizontal in range(3):
            x = horizontal * distanceBetweenCellsX + gridPosx
            y = vertical * distanceBetweenCellsY + gridPosy
            canvas.create_image(x, y, image=photo, anchor="c")
            canvas.create_text(x, y, text=texts[vertical*3+horizontal], font=('Arial', 28),
                               fill='white', anchor='c', tags=f"{vertical}_{horizontal}")

    # make the middle dial text bigger
    canvas.itemconfig("1_1", font=('Arial', 48, 'bold'))


canvas = Canvas(window, width=5000, height=5000)
canvas.config(bg='gray')
canvas.pack()

# Open and resize the image
image = Image.open('dial.png')
resized_image = image.resize((330, 196))

# Create the PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

findAllOutcomes()

window.mainloop()
