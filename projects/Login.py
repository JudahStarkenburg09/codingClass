import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x500")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=2000, height=2000)
canvas.pack()

# region User Symbol
# Create a cicle
circle = canvas.create_oval(66.7, 66.7, 133.3, 133.3, fill="gray", outline="gray", tags=('userSymbol'))
# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(50, 134, 150, 234, start=0, extent=180, fill="white", outline="gray", style="arc", width=4, tags=('userSymbol'))
#                                   X   Y   X    Y                        
line1 = canvas.create_line(48, 184, 152, 184, width=4, fill="gray", tags=('userSymbol'))
#                               X   Y    X    Y
# endregion

canvas.scale('userSymbol', 0, 0, .3, .3)  # shrink the size of the symbol
canvas.move('userSymbol', 100, 100)  # move the symbol with x, y directional pixel





# Start the Tkinter main loop
root.mainloop()
