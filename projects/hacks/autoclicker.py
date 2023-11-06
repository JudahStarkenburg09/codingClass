import tkinter as tk


main = tk.Tk()
main.geometry('450x300')
main.title("Advanced Autoclicker")
main.config(bg='gray')

amount = 1

def add():
    ''

def createText(text=None, posx=None, posy=None, center=False):
    if center:
        label = tk.Label(main, text=text, bg='gray')
        label.place(x=posx,y=posy, anchor='center')
    else:
        label = tk.Label(main, text=text, bg='gray')
        label.place(x=posx,y=posy)
    return label

def createInput(posx=None, posy=None, center=False):
    if center:
        entry = tk.Entry(main,bg='gray')
        entry.place(x=posx, y=posy, anchor='center')
    else:
        entry = tk.Entry(main,bg='gray')
        entry.place(x=posx, y=posy)
    return entry

def createButton(command, text=None, posx=None, posy=None, center=False, height=1):
    if center:
        button = tk.Button(main, text=text, command=lambda: command, bg='gray', height=height)
        button.place(x=posx, y=posy, anchor='center')
    else:
        button = tk.Button(main, text=text, command=lambda: command, bg='gray', height=height)
        button.place(x=posx, y=posy)
    return button

intervalText = createText(text="Interval (Microseconds): ", posx=0,posy=0, center=False)
interval = createInput(posx=145, posy=2, center=False)
startText = createText(text="Start after (Microseconds): ", posx=0, posy=25)
start = createInput(posx=145, posy=27, center=False)
addMore = createButton(posx=380, posy=10, text="Add Click", command=add())

main.mainloop()