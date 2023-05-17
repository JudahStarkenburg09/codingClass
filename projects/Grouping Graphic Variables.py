import tkinter as tk
light_gray = '#8A8A8A'
darkGray = '#343434'
clicks = 0
# Define the function to be executed when the button is clicked

# Create a Tkinter window
root = tk.Tk()
root.geometry("700x500")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()

rectIco = canvas.create_rectangle(50, 50, 150, 150, fill=light_gray, outline="", tags="menuIco")

# Create the horizontal lines
line1Ico = canvas.create_line(60, 80, 140, 80, width=4, fill=darkGray, tags="menuIco")
line2Ico = canvas.create_line(60, 100, 140, 100, width=4, fill=darkGray, tags="menuIco")
line3Ico = canvas.create_line(60, 120, 140, 120, width=4, fill=darkGray, tags="menuIco")

canvas.scale("home", 1, 1, 0.5, 0.4)

# Start the Tkinter main loop
root.mainloop()
