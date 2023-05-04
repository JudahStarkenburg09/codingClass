import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.geometry("200x230")
root.title("Change Circle By Percent")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()


coord1, coord2, coord3, coord4 = 10, 10, 60, 60 # ORIGINAL COORDINATES



# Calculate the new coordinates for a smaller circle
x1, y1, x2, y2 = canvas.bbox(canvas.create_oval(coord1, coord2, coord3, coord4))
cx = (x1 + x2) / 2  # x-coordinate of the center
cy = (y1 + y2) / 2  # y-coordinate of the center
w = x2 - x1  # width of the original circle
h = y2 - y1  # height of the original circle


percent = 70 # PERCENAGE TO CHANGE SMALLER


N = (100-percent)/100

w_new = w * N  # smaller width
h_new = h * N  # smaller height


x1_new = cx - w_new / 2  # new x-coordinate for the top-left corner
y1_new = cy - h_new / 2  # new y-coordinate for the top-left corner
x2_new = cx + w_new / 2  # new x-coordinate for the bottom-right corner
y2_new = cy + h_new / 2  # new y-coordinate for the bottom-right corner

# Create a smaller circle with the same center
circle = canvas.create_oval(x1_new, y1_new, x2_new, y2_new, fill="gray", outline="gray")
x1, y1, x2, y2 = canvas.bbox(canvas.create_oval(coord1, coord2, coord3, coord4))


def copy_to_clipboard():
    new_coords = f"{x1_new}, {y1_new}, {x2_new}, {y2_new}"
    root.clipboard_clear()
    root.clipboard_append(new_coords)

# Create a button to copy the new coordinates to the clipboard
button = tk.Button(root, text="Copy New Coordinates to Clipboard", command=copy_to_clipboard)
button.pack()

print(f"New Coords: {x1_new}, {y1_new}, {x2_new}, {y2_new},")

# Pack the canvas
canvas.pack()

# Start the Tkinter main loop
root.mainloop()
