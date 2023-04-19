import tkinter as tk
import io
from PIL import Image, ImageTk, ImageDraw

# Create a tkinter canvas and draw shapes on it
canvas_width = 300
canvas_height = 200
root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="red")
circle = canvas.create_oval(100, 50, 200, 150, fill="blue")

# Convert the canvas to a PIL image
ps = canvas.postscript(colormode='color')
img = Image.open(io.BytesIO(ps.encode('utf-8')))

# Save the combined image to a file
img.save('combined_image.png')

# Create a new Tkinter window and import the combined image
root2 = tk.Tk()
img2 = Image.open('combined_image.png')
tk_img = ImageTk.PhotoImage(img2)

# Create a label widget with the imported image
label = tk.Label(root2, image=tk_img)
label.pack()

root2.mainloop()
