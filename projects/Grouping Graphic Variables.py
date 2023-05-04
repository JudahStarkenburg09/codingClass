import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x500")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# region eye Symbol
# Create a cicle
# Create a cicle
circle = canvas.create_oval(27.2, 17.2, 42.8, 32.8, fill="black", outline="black", tags=('eyeShowPassword'))
# Create a half circle, Create a line to close off the bottom
half_circle = canvas.create_arc(0, 0, 70, 60, start=0, extent=180, fill="black", outline="black", style="arc", width=4, tags=('eyeShowPassword'))
rectToBindEye = canvas.create_rectangle(-5, -5, 75, 40, fill=None, outline=None, tags=('eyeShowPassword'))
#                                   X   Y   X    Y                        
#                               X   Y    X    Y
# endregion

canvas.scale('eyeShowPassword', 0, 0, 1, 1)  # shrink the size of the symbol
canvas.move('eyeShowPassword', 50, 50)  # move the symbol with x, y directional pixel





# Start the Tkinter main loop
root.mainloop()
