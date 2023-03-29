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
    percentages = [random.uniform(0, 100) for _ in range(9)]
    percentages[-1] = 100 - sum(percentages[:-1]) # Make sure percentages add up to 100
    
    dial_positions = [
        (160, 190), (410, 190), (660, 190),
        (40, 440), (160, 440), (410, 440), 
        (660, 440), (780, 440), (410, 690)
    ]
    
    dial_sizes = [
        (330, 196), (330, 196), (330, 196),
        (200, 120), (200, 120), (200, 120), 
        (200, 120), (200, 120), (330, 196)
    ]
    
    largest_percentage_index = percentages.index(max(percentages))
    
    for i, percentage in enumerate(percentages):
        dial_image = Image.open('dial.png')
        dial_image = dial_image.resize(dial_sizes[i])
        dial_photo = ImageTk.PhotoImage(dial_image)
        
        x, y = dial_positions[i]
        canvas.create_image(x, y, image=dial_photo)
        
        percentage_str = f"{percentage:.2f}%"
        canvas.create_text(x, y + dial_sizes[i][1] + 10, text=percentage_str, font=("Arial", 14), fill='white')
        
        if i == largest_percentage_index:
            canvas.create_oval(x-15, y-15, x+dial_sizes[i][0]+15, y+dial_sizes[i][1]+15, width=5, outline='white')
        

canvas = Canvas(window, width=5000, height=5000)
canvas.config(bg='gray')
canvas.pack()

findAllOutcomes()

window.mainloop()
