import tkinter as tk
import math

# Function to update the position of the smaller oval (Joystick) within the boundaries of the larger oval (joystickBase)
def move_joystick(event):
    # Get the coordinates of the mouse cursor
    x, y = event.x, event.y
    
    # Calculate the distance between the mouse cursor and the center of the joystickBase
    distance = ((x - 250) ** 2 + (y - 250) ** 2) ** 0.5
    
    # Check if the cursor is inside the joystickBase or at its border
    if distance <= 25:  # The radius of the joystickBase is 25
        joystick_x1, joystick_y1 = x - 25, y - 25
        joystick_x2, joystick_y2 = x + 25, y + 25
    else:
        # Calculate the angle between the cursor and the center of the joystickBase
        angle = math.atan2(y - 250, x - 250)
        
        # Calculate the new coordinates of the joystick (Joystick) to stay at the border of joystickBase
        joystick_x1 = int(250 + 25 * math.cos(angle)) - 25
        joystick_y1 = int(250 + 25 * math.sin(angle)) - 25
        joystick_x2 = int(250 + 25 * math.cos(angle)) + 25
        joystick_y2 = int(250 + 25 * math.sin(angle)) + 25

    # Update the position of the joystick (Joystick)
    canvas.coords(Joystick, joystick_x1, joystick_y1, joystick_x2, joystick_y2)

# Function to reset the position of the joystick (Joystick) to the center of the base (joystickBase)
def reset_joystick(event):
    canvas.coords(Joystick, 225, 225, 275, 275)

# Create the main window
root = tk.Tk()
root.title("Canvas Window")
root.geometry("500x500")

# Create a canvas widget
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Create the light gray oval in the center (joystickBase)
joystickBase = canvas.create_oval(200, 200, 300, 300, fill="light gray")

# Create the smaller dark gray oval (Joystick)
Joystick = canvas.create_oval(225, 225, 275, 275, fill="dark gray")

# Bind mouse dragging events to the smaller oval (Joystick)
canvas.tag_bind(Joystick, "<Button1-Motion>", move_joystick)

# Bind mouse release event to reset the position of the joystick (Joystick) to the center of the base (joystickBase)
canvas.tag_bind(Joystick, "<ButtonRelease-1>", reset_joystick)

# Start the main loop
root.mainloop()
