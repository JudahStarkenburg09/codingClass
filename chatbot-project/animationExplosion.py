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


animateLocation = [50, 50]

images = [
    {
        "image": "explosion1.png",
        "location": ((animateLocation[0]+24), (animateLocation[1]-43))
    },
    {
        "image": "explosion2.png",
        "location": (animateLocation[0]-5, animateLocation[1]-2)
    },
    {
        "image": "explosion3.png",
        "location": (animateLocation[0]-15, animateLocation[1]-5)
    },
    {
        "image": "explosion4.png",
        "location": (animateLocation[0]-15, animateLocation[1]-45)
    },
    {
        "image": "explosion5.png",
        "location": (animateLocation[0]-15, animateLocation[1]-35)
    },
    {
        "image": "explosion6.png",
        "location": (animateLocation[0], animateLocation[1])
    },
    {
        "image": "explosion7.png",
        "location": (animateLocation[0]-10, animateLocation[1])
    },
]



def explode():
    animate = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for i in range(7):
            screen.fill((0, 0, 0)) # Erase the screen
            animatedImage = pygame.image.load((images[i])["image"])
            screen.blit(animatedImage, ((images[i]))["location"])
            pygame.draw.circle(screen, (100, 100, 255), (140, 140), 10)
            pygame.display.update()  # update the screen 
            pygame.display.flip()
            pygame.time.delay(70)  # pause for 70 milliseconds (0.07 seconds)
        
        input('')
        


explode()
