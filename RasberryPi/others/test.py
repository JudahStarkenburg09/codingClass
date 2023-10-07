import tkinter as tk
import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# List the available joystick devices
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Initialize all detected joysticks
for joystick in joysticks:
    joystick.init()

# Create the main window
root = tk.Tk()
root.title("Joystick Control")
root.geometry("800x500")  # Increase the width of the window

# Create a canvas widget for the left joystick (joystickBaseLeft)
canvas_left = tk.Canvas(root, width=400, height=500)
canvas_left.pack(side=tk.LEFT)  # Place it on the left side of the window

# Create the light gray oval for the left joystick base (joystickBaseLeft)
joystickBaseLeft = canvas_left.create_oval(100, 200, 200, 300, fill="light gray")

# Create the smaller dark gray oval for the left joystick (JoystickLeft)
JoystickLeft = canvas_left.create_oval(125, 225, 175, 275, fill="dark gray")

# Create a canvas widget for the right joystick (joystickBaseRight)
canvas_right = tk.Canvas(root, width=400, height=500)
canvas_right.pack(side=tk.LEFT)  # Place it on the right side of the window

# Create the light gray oval for the right joystick base (joystickBaseRight)
joystickBaseRight = canvas_right.create_oval(100, 200, 200, 300, fill="light gray")

# Create the smaller dark gray oval for the right joystick (JoystickRight)
JoystickRight = canvas_right.create_oval(125, 225, 175, 275, fill="dark gray")

# Function to update the position of the left joystick (JoystickLeft) within the boundaries of the left joystick base (joystickBaseLeft)
def move_joystick_left(event):
    # Get the coordinates of the mouse cursor
    x, y = event.x, event.y
    
    # Calculate the distance between the mouse cursor and the center of the left joystick base (joystickBaseLeft)
    distance = ((x - 150) ** 2 + (y - 250) ** 2) ** 0.5
    
    # Check if the cursor is inside the left joystick base (joystickBaseLeft) or at its border
    if distance <= 25:  # The radius of the left joystick base (joystickBaseLeft) is 25
        joystick_x1, joystick_y1 = x - 25, y - 25
        joystick_x2, joystick_y2 = x + 25, y + 25
    else:
        # Calculate the angle between the cursor and the center of the left joystick base (joystickBaseLeft)
        angle = pygame.math.Vector2(x - 150, y - 250).angle_to(pygame.math.Vector2(1, 0))
        radians = pygame.math.Vector2(x - 150, y - 250).length() / 25
        radians = min(max(radians, 0), 1)
        joystick_x1 = 150 + (25 * radians * pygame.math.Vector2(1, 0)).x - 25
        joystick_y1 = 250 + (25 * radians * pygame.math.Vector2(1, 0)).y - 25
        joystick_x2 = 150 + (25 * radians * pygame.math.Vector2(1, 0)).x + 25
        joystick_y2 = 250 + (25 * radians * pygame.math.Vector2(1, 0)).y + 25

    # Update the position of the left joystick (JoystickLeft)
    canvas_left.coords(JoystickLeft, joystick_x1, joystick_y1, joystick_x2, joystick_y2)

# Bind mouse dragging events to the left joystick (JoystickLeft)
canvas_left.tag_bind(JoystickLeft, "<Button1-Motion>", move_joystick_left)

# Function to update the position of the right joystick (JoystickRight) within the boundaries of the right joystick base (joystickBaseRight)
def move_joystick_right(event):
    # Get the coordinates of the mouse cursor
    x, y = event.x, event.y
    
    # Calculate the distance between the mouse cursor and the center of the right joystick base (joystickBaseRight)
    distance = ((x - 550) ** 2 + (y - 250) ** 2) ** 0.5
    
    # Check if the cursor is inside the right joystick base (joystickBaseRight) or at its border
    if distance <= 25:  # The radius of the right joystick base (joystickBaseRight) is 25
        joystick_x1, joystick_y1 = x - 25, y - 25
        joystick_x2, joystick_y2 = x + 25, y + 25
    else:
        # Calculate the angle between the cursor and the center of the right joystick base (joystickBaseRight)
        angle = pygame.math.Vector2(x - 550, y - 250).angle_to(pygame.math.Vector2(1, 0))
        radians = pygame.math.Vector2(x - 550, y - 250).length() / 25
        radians = min(max(radians, 0), 1)
        joystick_x1 = 550 + (25 * radians * pygame.math.Vector2(1, 0)).x - 25
        joystick_y1 = 250 + (25 * radians * pygame.math.Vector2(1, 0)).y - 25
        joystick_x2 = 550 + (25 * radians * pygame.math.Vector2(1, 0)).x + 25
        joystick_y2 = 250 + (25 * radians * pygame.math.Vector2(1, 0)).y + 25

    # Update the position of the right joystick (JoystickRight)
    canvas_right.coords(JoystickRight, joystick_x1, joystick_y1, joystick_x2, joystick_y2)

# Bind mouse dragging events to the right joystick (JoystickRight)
canvas_right.tag_bind(JoystickRight, "<Button1-Motion>", move_joystick_right)

# Main event loop
def update_joystick_position():
    while True:
        pygame.event.get()  # Get joystick events

        # Access axis values for the left joystick
        for joystick in joysticks:
            axis_x_left = joystick.get_axis(0)  # X-axis (left-right) for the left joystick
            axis_y_left = -joystick.get_axis(1)  # Y-axis (up-down) for the left joystick, invert Y-axis
            axis_y_left *= -1

            # Calculate the position based on left joystick input
            max_displacement_left = 25  # Maximum displacement for the left joystick
            new_x_left = 150 + int(max_displacement_left * axis_x_left)
            new_y_left = 250 + int(max_displacement_left * axis_y_left)

            # Ensure the left joystick (JoystickLeft) stays within the left joystick base (joystickBaseLeft)
            if new_x_left < 125:
                new_x_left = 125
            elif new_x_left > 175:
                new_x_left = 175
            if new_y_left < 225:
                new_y_left = 225
            elif new_y_left > 275:
                new_y_left = 275

            # Update the position of the left joystick (JoystickLeft)
            canvas_left.coords(JoystickLeft, new_x_left - 25, new_y_left - 25, new_x_left + 25, new_y_left + 25)

        # Access axis values for the right joystick
        for joystick in joysticks:
            axis_x_right = joystick.get_axis(2)  # X-axis (left-right) for the right joystick
            axis_y_right = -joystick.get_axis(3)  # Y-axis (up-down) for the right joystick, invert Y-axis
            axis_y_right *= -1

            # Calculate the position based on right joystick input
            max_displacement_right = 25  # Maximum displacement for the right joystick
            new_x_right = 550 + int(max_displacement_right * axis_x_right)
            new_y_right = 250 + int(max_displacement_right * axis_y_right)

            # Ensure the right joystick (JoystickRight) stays within the right joystick base (joystickBaseRight)
            if new_x_right < 525:
                new_x_right = 525
            elif new_x_right > 575:
                new_x_right = 575
            if new_y_right < 225:
                new_y_right = 225
            elif new_y_right > 275:
                new_y_right = 275

            # Update the position of the right joystick (JoystickRight)
            canvas_right.coords(JoystickRight, new_x_right - 25, new_y_right - 25, new_x_right + 25, new_y_right + 25)

        root.update_idletasks()  # Update the tkinter window

# Start a thread to continuously update the joystick position
import threading
joystick_thread = threading.Thread(target=update_joystick_position)
joystick_thread.daemon = True
joystick_thread.start()

# Start the main tkinter loop
root.mainloop()
