from tkinter import *
import tkinter as tk
import random
import os
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry('800x800')
window.title("Time Teller App")
window.config(bg='gray')

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

def findAllOutcomes():
    for i in range(1,9):
        y, m, d, h = random.randrange(1,70), random.randrange(1,11), random.randrange(1,28), random.randrange(1,23)
        image = Image.open("dial.png")
        dial = ImageTk.PhotoImage(image)

        label = tk.Label(window, image=dial)
        label.image = dial

        label.place(x=50, y=50)


findAllOutcomes()



window.mainloop()