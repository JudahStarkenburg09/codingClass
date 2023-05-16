import tkinter as tk
light_gray = '#8A8A8A'
clicks = 0
# Define the function to be executed when the button is clicked

# Create a Tkinter window
root = tk.Tk()
root.geometry("700x500")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()

left_rectangle = canvas.create_rectangle(50, 100, 75, 150, fill=light_gray, outline="",tags="home")
right_rectangle = canvas.create_rectangle(95, 100, 120, 150, fill=light_gray, outline="", tags="home")

# Create the roof triangle of the home symbol
roof_triangle = canvas.create_polygon(30, 100, 85, 30, 140, 100, fill=light_gray, outline="", tags="home")
canvas.scale("home", 1, 1, 0.5, 0.4)

# Start the Tkinter main loop
root.mainloop()
