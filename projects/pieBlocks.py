import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Simulation")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Create blocks
block1_mass = 1
block1_width = 40
block1_height = 40
block1_x = 50
block1_y = screen_height - block1_height
block1_vx = 1 if block1_mass == 1 else 0

block2_mass = 100000
block2_width = 40
block2_height = 40
block2_x = 300
block2_y = screen_height - block2_height
block2_vx = 0

# Create wall
wall_color = (0, 0, 0)
wall_thickness = 5

def draw_wall():
    pygame.draw.line(screen, wall_color, (0, 0), (0, screen_height), wall_thickness)

# Main loop
def main():
    global block1_x, block2_x, block1_vx, block2_vx
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        draw_wall()
# i fixed it, but i want the red one to start moving first, and when it hits the blue one, transfer velocity like elastic movment and physics in real life would, but add a feature to change the weight, and make the text showing the weight in a text box attached to the boxes 
        # Update block positions
        block1_x += block1_vx
        block2_x += block2_vx

        # Check collisions
        if block1_x + block1_width >= block2_x:
            block1_vx *= -1
            block2_vx *= -1

        if block1_x <= 0:
            block1_vx *= -1

        # Draw blocks
        pygame.draw.rect(screen, blue, (block1_x, block1_y, block1_width, block1_height))
        pygame.draw.rect(screen, red, (block2_x, block2_y, block2_width, block2_height))

        pygame.display.update()
        clock.tick(60)

main()
