import tkinter as tk
from tkinter import font
import time

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

import tkinter as tk
from tkinter import font

# Print available font families
print(font.families())

# Rest of your code
# ...


# Load the digital-7.ttf font file
try:
    digital_font = font.Font(family='ds-digital', size=50)
    print("Success")
except tk.TclError:
    print("Error: Unable to load the font. Make sure 'digital-7.ttf' is in the same directory as your script.")

# Create a label for displaying the time
label = tk.Label(root, font=digital_font, background="black", foreground="green")
label.pack(padx=20, pady=20)

# Run the update_time function to initialize the time display
update_time()

# Set the window background color
root.configure(bg="black")

# Run the Tkinter event loop
root.mainloop()
