import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)

fingerAmountLeft = 5
fingerAmountRight = 5

botFingerAmountLeft = 5
botFingerAmountRight = 5

def drawPlayerFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 525, 25, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 525), 12.5)

def drawBotFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 0, 25, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 75), 12.5)

# Define a function for button actions
def button_action(bn):
    print(f"Button {bn} clicked")

selected1 = 'yellow'
selected2 = 'yellow'
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

    # Draw buttons and check for clicks
    b1 = pygame.draw.rect(screen, (255, 255, 0), (110, 100, 50, 50))
    b2 = pygame.draw.rect(screen, (255, 255, 0), (650, 100, 50, 50))
    b3 = pygame.draw.rect(screen, selected1, (110, 450, 50, 50))
    b4 = pygame.draw.rect(screen, selected2, (650, 450, 50, 50))

    for i in range(1, 5):
        button_rect = globals()[f"b{i}"]
        if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(mouse_x, mouse_y):
            button_action(i)

    pygame.display.flip()

pygame.quit()
sys.exit()
