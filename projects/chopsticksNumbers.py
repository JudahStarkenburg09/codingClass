import pygame
import sys
import time

pygame.init()

# Screen dimensions
width, height = 810, 610
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chopsticks")

# Create fonts
font = pygame.font.Font(None, 72)  # Increased font size

# Define colors
YELLOW = (255, 255, 0)

# Initialize variables
botLeft = 1
botRight = 1
playerLeft = 1
playerRight = 1

def buttonAction(buttonIndex):
    global botLeft, botRight, playerLeft, playerRight

# Main game loop
mouseButtonDown = False
buttonClicked = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button down
            for i in range(4):
                if buttons[i].collidepoint(event.pos):
                    buttonClicked = i

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button up
            if buttonClicked is not None:
                buttonAction(buttonClicked)
                buttonClicked = None

    # Calculate button dimensions and positions
    button_width = (width - 60) // 2  # Reduced button size to 3/4
    button_height = (height - 60) // 2  # Reduced button size to 3/4
    button_x = [30, width // 2 + 30, 30, width // 2 + 30]
    button_y = [30, 30, height // 2 + 30, height // 2 + 30]

    # Create buttons
    buttons = []
    for i in range(4):
        button = pygame.Rect(button_x[i], button_y[i], button_width, button_height)
        buttons.append(button)

    # Draw buttons with text
    screen.fill((255, 255, 255))
    for i in range(4):
        pygame.draw.rect(screen, YELLOW, buttons[i])
        text = font.render(str([botLeft, botRight, playerLeft, playerRight][i]), True, (0, 0, 0))
        text_rect = text.get_rect(center=buttons[i].center)
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
