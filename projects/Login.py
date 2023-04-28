import tkinter as tk

light_gray = '#8A8A8A' #Order from lightest to darkest
lighterish_gray = '#4D4D4D'
lightish_gray = '#3F3F3F'
darkGray = '#343434'
font = ("Arial", 15)

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x400")
root.config(bg=darkGray)

# Create a canvas to draw on
canvas = tk.Canvas(root, width=2000, height=2000)
canvas.config(bg=darkGray)
canvas.pack()

rect1 = canvas.create_rectangle(0, 100, 500, 150, fill=lightish_gray, outline=lighterish_gray, width=.5)
rect2 = canvas.create_rectangle(0, 150, 500, 200, fill=lightish_gray, outline=lighterish_gray, width=.5)

# region User Symbol


# Create a cicle
circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill=None, outline=light_gray, width=1.5, tags=('userSymbol'))

# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill=None, outline=light_gray, style="arc", width=1.5, tags=('userSymbol'))
#                                X   Y   X    Y                        
line1 = canvas.create_line(48, 184, 152, 184, width=1.5, fill=light_gray, tags=('userSymbol'))
#                           X   Y    X    Y


# endregion

canvas.scale('userSymbol', 0, 0, .18, .18)  # shrink the size of the symbol
canvas.move('userSymbol', 33, 101)



# Create entry box with initial text and color
username_entry = tk.Entry(canvas, width=37, fg=light_gray, font=font, bd=0, insertbackground=lighterish_gray) #border=.5,)
username_entry.insert(0, 'Username')
username_entry.configure({"background": lightish_gray})

# Define functions to handle focus and unfocus events
def on_entry_click(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, "end") # Delete all the text in the entry
        username_entry.configure(fg=light_gray)

def on_entry_unfocus(event):
    if username_entry.get() == '':
        username_entry.configure(fg=lightish_gray)
        username_entry.insert(0, 'Username')

# Bind focus and unfocus events to entry box
username_entry.bind('<FocusIn>', on_entry_click)
username_entry.bind('<FocusOut>', on_entry_unfocus)

# Place entry box on canvas
canvas.create_window(280, 125, window=username_entry)




# Start the Tkinter main loop
root.mainloop()
