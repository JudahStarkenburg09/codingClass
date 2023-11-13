import tkinter as tk
from tkinter import messagebox
from tkinter import *

main = tk.Tk()
main.geometry('450x300')
main.title("Advanced Autoclicker")
main.config(bg='white')
dropdownVar1 = None
dropdownVar2 = None
dropdownVar3 = None
dropdownVar4 = None
dropdownVar5 = None
def on_option_select(event):
    if globals()[f"dropdownVar1"].get() == "Other...":
        print("1 is other")

amount = 0
options = ["Right click", "Left click", "Middle Click", "Space Bar", "Other..."]
def add():
    global amount
    amount += 1
    if amount > 5:
        messagebox.showerror("Error", "Too many already made!")
        amount = 5

    for i in range(0, amount):
        main.geometry(f'450x{100+(100*i)}')
        globals()[f'intervalText_{i}'] = createText(text="Interval (Microseconds): ", posx=0, posy=0+(100*i), center=False)
        globals()[f'interval_{i}'] = createInput(posx=145, posy=2+(100*i), center=False)
        globals()[f'startText_{i}'] = createText(text="Start after (Microseconds): ", posx=0, posy=25+(100*i))
        globals()[f'startAfter_{i}'] = createInput(posx=145, posy=27+(100*i), center=False)
        globals()[f"dropdownVar{i}"] = StringVar(main)
        eval(f"dropdownVar{i}.set(options[0])")
        globals()[f"dropdown{i}"] = OptionMenu(main, globals()[f"dropdownVar{i}"], *options, command=on_option_select)
        
    print(f"clicked, now there are {i+1} sets")


def createText(text=None, posx=None, posy=None, center=False):
    if center:
        label = tk.Label(main, text=text, bg='white')
        label.place(x=posx,y=posy, anchor='center')
    else:
        label = tk.Label(main, text=text, bg='white')
        label.place(x=posx,y=posy)
    return label

def createInput(posx=None, posy=None, center=False):
    if center:
        entry = tk.Entry(main,bg='white')
        entry.place(x=posx, y=posy, anchor='center')
    else:
        entry = tk.Entry(main,bg='white')
        entry.place(x=posx, y=posy)
    return entry

def createButton(command, text=None, posx=None, posy=None, center=False, height=1):
    if center:
        button = tk.Button(main, text=text, command=lambda: command, bg='white', height=height)
        button.place(x=posx, y=posy, anchor='center')
    else:
        button = tk.Button(main, text=text, command=lambda: command, bg='white', height=height)
        button.place(x=posx, y=posy)
    return button


button = tk.Button(main, text="Add Click", command=lambda: add(), bg='white')
button.place(x=380, y=10, anchor='center')
add()

main.mainloop()