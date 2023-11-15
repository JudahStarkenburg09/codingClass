import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

# Replace 'path_to_your_image' with the actual path to your image file
image_path = 'NCASymbol.png'
desired_width = 50  # Replace with your preferred width in pixels
desired_height = 50  # Replace with your preferred height in pixels

# Create the main Tkinter window
window = tk.Tk()
window.title("Image Resizing Example")

# Load and resize the image
tk_image = resize_image(image_path, desired_width, desired_height)

# Create a Tkinter label and display the image at specified (x, y) coordinates
x_coordinate = 50  # Replace with your desired x-coordinate
y_coordinate = 50  # Replace with your desired y-coordinate
image_label = tk.Label(window, image=tk_image)
image_label.place(x=x_coordinate, y=y_coordinate)

# Run the Tkinter event loop
window.mainloop()
