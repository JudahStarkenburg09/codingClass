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
    percentages = [random.randint(1, 100) for _ in range(9)]
    total = sum(percentages)
    # Normalize the percentages so that they add up to 100
    percentages = [int(p/total*100) for p in percentages]
    # Sort the percentages in decreasing order
    percentages.sort(reverse=True)
    return percentages


def findAllOutcomes():
    percentages = generate_percentages()
    # Set the largest percentage as the middle text
    middleText = str(percentages[0]) + '%'
    # Set the other 8 percentages as the small texts
    smallTexts = [str(p) + '%' for p in percentages[1:]]
    # Make a grid?
    for vertical in range(3):
        # Increase vertical direction to make 3x3 grid
        for horizontal in range(3):
            gridPosx, gridPosy = (160, 190) #GRID POSITION
            distanceBetweenCellsX, distanceBetweenCellsY = (250, 250) #DISTANCE BETWEEN GRID CELLS
            
            x = horizontal * distanceBetweenCellsX + gridPosx
            y = vertical * distanceBetweenCellsY + gridPosy
            canvas.create_image(x, y, image=photo)
    
    # Create the middle dial
    canvas.create_text(400, 400, text=middleText, font=('Arial', 48, 'bold'), fill='white')
    
    # Create the other 8 small dials
    for i, text in enumerate(smallTexts):
        x = (i%3)*distanceBetweenCellsX + gridPosx
        y = (i//3)*distanceBetweenCellsY + gridPosy + 140
        canvas.create_text(x, y, text=text, font=('Arial', 28), fill='white')
    
    canvas.create_rectangle(295, 350, 505, 540, fill='gray', outline='gray')


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
