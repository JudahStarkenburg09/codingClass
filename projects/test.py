import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

item_list = ["Item 1", "Item 2", "Item 3", 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Rotation speed (in degrees per frame)
rotation_slowdown = input("Enter speed, 1-5: ")  # Adjust this value to control the rotation speed
rotation_speed = 3

def spin(item_list, rotation_speed, rotation_slowdown):
    rotation_slowdown = int(rotation_slowdown)
    rotation_slowdown = 1/(10**(rotation_slowdown/(2+random.uniform(0,1.5))))
    print(f"{rotation_slowdown}")
    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rotating Circle with Lines")

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

    # Draw the lines inside the circle
    for i in range(num_lines):
        angle = (360 / num_lines) * i
        x1 = circle_radius
        y1 = circle_radius
        x2 = circle_radius + circle_radius * math.cos(math.radians(angle))
        y2 = circle_radius + circle_radius * math.sin(math.radians(angle))
        pygame.draw.line(circle_surface, black, (x1, y1), (x2, y2), 2)

    # Draw the circle
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




        

        # Rotate the circle surface with lines
        rotated_circle = pygame.transform.rotate(circle_surface, rotation_angle)
        rotated_rect = rotated_circle.get_rect(center=circle_center)
        screen.blit(rotated_circle, rotated_rect.topleft)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

spin(item_list, rotation_speed, rotation_slowdown)
