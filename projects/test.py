import tkinter as tk


darkGray = '#404040'
light_gray = '#BEBEBE'
extra_light_gray = '#F0F0F0'


root = tk.Tk()
root.geometry('300x200')

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Create entry box with initial text and color
username_entry = tk.Entry(canvas, width=30, fg=light_gray, insertbackground=light_gray)
username_entry.insert(0, 'Username')
username_entry.configure({"background": extra_light_gray})

# Define functions to handle focus and unfocus events
def on_entry_click(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, "end") # Delete all the text in the entry
        username_entry.configure(fg=light_gray)

def on_entry_unfocus(event):
    if username_entry.get() == '':
        username_entry.configure(fg=extra_light_gray)
        username_entry.insert(0, 'Username')

# Bind focus and unfocus events to entry box
username_entry.bind('<FocusIn>', on_entry_click)
username_entry.bind('<FocusOut>', on_entry_unfocus)

# Place entry box on canvas
canvas.create_window(150, 100, window=username_entry)

root.mainloop()
