import tkinter as tk

root = tk.Tk()
root.geometry('500x400')
root.title(" ")


def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)

# Bind F11 key to toggle fullscreen
root.bind("<F11>", toggle_fullscreen)

# Bind Escape key to exit fullscreen
root.bind("<Escape>", toggle_fullscreen)

canvas = tk.Canvas(width=10000, height=10000, bg='black')
canvas.pack()



root.mainloop()