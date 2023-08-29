import pygame
import time



pygame.init()


width, height = 500, 500
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 30)
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 128, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(128, 0, 128)
violet = pygame.Color(238, 130, 238)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(100, 100, 100)
dGray = pygame.Color(50, 50, 50)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(dGray)

    for layer in range(3):
        for v in range(0, height // 5):
            for h in range(0, width // 5):
                pygame.draw.rect(screen, (255, 255, 255), (h * 5 + layer * 3, v * 5 + layer * 3, 5, 5))

    time.sleep(0.01)
    pygame.display.flip()

# Quit pygame
pygame.quit()