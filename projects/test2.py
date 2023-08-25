import tkinter as tk
from tkinter import *
import random

while True:
    answer = random.randint(1,100)
    while True:

        root = tk.Tk()
        root.title('test')
        root.geometry('200x200')


        def click():
            global label1, user
            text = user.get()
            if not text.isdigit():
                label1.config(text="Must be a number between 1-100!")
                break
                
            if text > 100 or text < 1:
                label1.config(text="Must be a number between 1-100")





            label1.config(text=f"{text}")

        label1 = Label(root, text='Enter A Number 1-100')
        label1.place(x=10, y=10)

        user = Entry(root)
        user.place(x=10, y=50)

        root.bind("<Return>", lambda event: click())

        root.mainloop()