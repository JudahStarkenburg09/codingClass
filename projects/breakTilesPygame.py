import pygame
import time
import math

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
violet = (238, 130, 238)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
dGray = (50, 50, 50)

clock = pygame.time.Clock()
FPS = 120
pygame.display.set_caption('Ball shooter')

spacing = 5
rect_width = 10
rect_height = 10

def shoot():
    print("shot")
    return

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            if event.button == 1:  # Left mouse button
                shoot()

    screen.fill(dGray)


    y_position = spacing  # Start position
    for _ in range(10):
        x_position = spacing  # Start position
        for _ in range(33):
            pygame.draw.rect(screen, blue, (x_position, y_position, rect_width, rect_height))
            x_position += rect_width + spacing
        y_position += rect_height + spacing
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_y = max(mouse_y, height // 2)
    center_x = width // 2
    center_y = height - rect_height // 2
    pygame.draw.line(screen, red, (center_x, center_y), (mouse_x, mouse_y), 2)

    # Calculate the angle for the arrow
    angle = math.atan2(mouse_y - center_y, mouse_x - center_x)
    arrow_length = 20
    arrow_x = mouse_x - arrow_length * math.cos(angle)
    arrow_y = mouse_y - arrow_length * math.sin(angle)

    # Draw the arrow
    pygame.draw.line(screen, red, (mouse_x, mouse_y), (arrow_x, arrow_y), 2)
    # pygame.draw.polygon(screen, red, [(arrow_x, arrow_y), (arrow_x + 5, arrow_y + 15), (arrow_x - 5, arrow_y + 15)])

    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
