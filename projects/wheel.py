import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

rotation_slowdown = 0
rotation_speed = 0
item_list = ["Item 1", "Item 2", "Item 3"]
# Rotation speed (in degrees per frame)


def spin(item_list, rotation_speed, rotation_slowdown):
    slows = [
        {
        "input": 1,
        "slowdown": .001,
        },
        {
        "input": 2,
        "slowdown": .0005,
        },
        {
        "input": 3,
        "slowdown": .0001,
        },
        {
        "input": 4,
        "slowdown": .00005,
        },
        {
        "input": 5,
        "slowdown": .00001,
        },
    ]
    speeds = [
        {
            "input": 1,
            "speed": 2,
        },
        {
            "input": 2,
            "speed": 2,
        },
        {
            "input": 3,
            "speed": 3,
        },
        {
            "input": 4,
            "speed": 3,
        },
        {
            "input": 5,
            "speed": 4,
        },
    ]

    rotation_objects = input("Enter 'speed , time': ")

    # Remove spaces and split the input by comma
    rotation_objects = rotation_objects.replace(" ", "").split(",")
    chose = False
    for i in slows:
        print(str(i["input"]) + " =? " + rotation_objects[1])
        if rotation_objects[1] == str(i["input"]):
            rotation_slowdown = i["slowdown"] + random.uniform(0, 0.0001)
            chose = True
            print("found")
    if chose == False:
        return "Time must be 1-5!"
    
    chose = False
    for d in speeds:
        if rotation_objects[0] == str(d["input"]):
            rotation_speed = d["speed"] + random.uniform(0, 0.05)
            chose = True
    if chose == False:
        return "Speed must be 1-5!"
    
    print(rotation_speed, rotation_slowdown)



    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rotating Circle with Items")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Circle properties
    circle_radius = 200
    circle_center = (width // 2, height // 2)

    # Line properties
    num_lines = len(item_list)

    # Define the initial rotation angle
    rotation_angle = 0

    # Create a surface for the circle with lines
    circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)

    # Draw the lines inside the circle and place items between the lines
    for i in range(num_lines):
        angle = (360 / num_lines) * i
        x1 = circle_radius
        y1 = circle_radius
        x2 = circle_radius + circle_radius * math.cos(math.radians(angle))
        y2 = circle_radius + circle_radius * math.sin(math.radians(angle))
        
        # Calculate item position
        item_angle = (angle + (360 / num_lines) / 2)  # Place item in the middle of each segment
        item_x = circle_radius + circle_radius * 0.7 * math.cos(math.radians(item_angle))
        item_y = circle_radius + circle_radius * 0.7 * math.sin(math.radians(item_angle))

        # Draw a line and place item text
        pygame.draw.line(circle_surface, black, (x1, y1), (x2, y2), 2)
        font = pygame.font.Font(None, 24)  # Adjust font size as needed
        item_text = item_list[i]
        text_surface = font.render(item_text, True, black)
        text_rect = text_surface.get_rect(center=(item_x, item_y))
        circle_surface.blit(text_surface, text_rect.topleft)

    # Draw the circle on top of the lines and items
    pygame.draw.circle(circle_surface, black, (circle_radius, circle_radius), circle_radius, 2)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(white)
        if rotation_speed <= 0:
            rotation_speed = 0
        else:
            # Update the rotation angle
            rotation_angle += rotation_speed
            rotation_speed -= rotation_slowdown
            print(f"Current Speed: [{rotation_speed}], Slowing Down At: [{rotation_slowdown}]")

        # Rotate the circle surface with lines and items
        rotated_circle = pygame.transform.rotate(circle_surface, rotation_angle)
        rotated_rect = rotated_circle.get_rect(center=circle_center)
        screen.blit(rotated_circle, rotated_rect.topleft)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

spin(item_list, rotation_speed, rotation_slowdown)
