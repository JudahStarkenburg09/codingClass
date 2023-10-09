import typeData
import graphics
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Window")

# Define colors
WHITE = (255, 255, 255)

# Function to handle key presses
def handle_key_press(key):
    for i in ('abcdefghijklmnopqrstuvwxyz'):
        CKey = getattr(pygame, f"K_{i}")
        if key == CKey:
            print(i)
        elif key == pygame.K_SPACE:
            i = ' '
            print('space')
        if i == nextKey:
            ''
    # Add more keys as needed
sentence = typeData.sentenceEquals()
# Main game loop
running = True
while running:
    nextKey = typeData.getNextKey()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_key_press(event.key)

    # Fill the background with white
    window.fill(WHITE)

    # Update the display
    pygame.display.flip()

# Quit pygame and close the window
pygame.quit()
sys.exit()
