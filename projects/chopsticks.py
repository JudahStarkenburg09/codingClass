import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)

fingerAmountLeft = 1
fingerAmountRight = 1

botFingerAmountLeft = 1
botFingerAmountRight = 1

def drawPlayerFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 525, 25, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 525), 12.5)

def drawBotFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 0, 25, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 75), 12.5)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Clear the screen
    screen.fill(WHITE)

    for i in range(0, fingerAmountLeft):
        xr = 50 + (i*40)
        xa = 62.5 + (i*40)
        drawPlayerFinger(xr, xa)

    for i in range(0, fingerAmountRight):
        xr = 725 - (i*40)
        xa = 737.5 - (i*40)
        drawPlayerFinger(xr, xa)

    for i in range(0, botFingerAmountLeft):
        xr = 50 + (i*40)
        xa = 62.5 + (i*40)
        drawBotFinger(xr, xa)

    for i in range(0, botFingerAmountRight):
        xr = 725 - (i*40)
        xa = 737.5 - (i*40)
        drawBotFinger(xr, xa)

    pygame.draw.rect(screen, (100, 255, 50),)

    

    pygame.display.flip()

pygame.quit()
sys.exit()
