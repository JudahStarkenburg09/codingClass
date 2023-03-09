import os
import pygame

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0)) # Erase the screen

# Create a clock to control the frame rate
clock = pygame.time.Clock()

def explode():
    animate = 0
    while animate < 7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0, 0, 0)) # Erase the screen
        animate += 1
        animatedImage = pygame.image.load(f'explosion{animate}.png')
        screen.blit(animatedImage, (50, 50))
        pygame.display.update()  # update the screen 
        pygame.display.flip()

        pygame.time.delay(100)  # pause for 100 milliseconds (0.1 seconds)


explode()
