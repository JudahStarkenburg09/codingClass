import pyautogui
import time
import tkinter as tk

window = tk.Tk()
window.geometry('300x200')
window.title("Auto Keyer")

miliText = tk.Label(window, text="Enter Time (Miliseconds)")
miliText.place(x=10, y=10)

miliTime = tk.Entry(window, width=7)
miliTime.place(x=150, y=10)



window.mainloop()