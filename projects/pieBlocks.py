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
block2_mass_red = 1
speed = -1


block1_width = 40
block1_height = 40
block1_x = 50
block1_y = screen_height - block1_height
block1_vx = 0

block2_width = 40
block2_height = 40
block2_x = 300
block2_y = screen_height - block2_height
block2_vx = speed
collision_count = 0

# Create wall
wall_color = (0, 0, 0)
wall_thickness = 5

# Create font
font = pygame.font.Font(None, 36)

def draw_wall():
    pygame.draw.line(screen, wall_color, (0, 0), (0, screen_height), wall_thickness)

def draw_weights():
    text_block1 = font.render(f"Block 1 Weight: {block1_mass}", True, blue)
    text_block2 = font.render(f"Block 2 Weight: {block2_mass_red}", True, red)
    screen.blit(text_block1, (20, 20))
    screen.blit(text_block2, (20, 60))

def update_velocity(m1, v1, m2, v2):
    new_v1 = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
    new_v2 = (2 * m1 / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
    return new_v1, new_v2

# Main loop
def main():
    global block1_x, block2_x, block1_vx, block2_vx, block1_mass, block2_mass_red
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        draw_wall()
        draw_weights()

        # Update block positions
        block1_x += block1_vx
        block2_x += block2_vx

        # Check collisions
        if block1_x + block1_width >= block2_x:
            block1_vx, block2_vx = update_velocity(block1_mass, block1_vx, block2_mass_red, block2_vx)

        if block1_x <= 0:
            block1_vx *= -1

        # Draw blocks
        pygame.draw.rect(screen, blue, (block1_x, block1_y, block1_width, block1_height))
        pygame.draw.rect(screen, red, (block2_x, block2_y, block2_width, block2_height))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
