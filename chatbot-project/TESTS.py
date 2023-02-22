import pygame
import os
import sys
pygame.init()

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the road image
road_image = pygame.image.load("road.png").convert()

# Resize the road image to fit the screen width
road_image = pygame.transform.scale(road_image, (SCREEN_WIDTH, road_image.get_height()))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Set the initial position of the road image
road_pos = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scroll the road image
    road_pos += 2
    if road_pos > SCREEN_WIDTH:
        road_pos = 0

    # Draw the road image
    screen.blit(road_image, (road_pos - SCREEN_WIDTH, 0))
    screen.blit(road_image, (road_pos, 0))

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
