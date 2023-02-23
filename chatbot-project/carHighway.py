import pygame
import os
import sys
pygame.init()

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

# Set up the screen
SCREEN_WIDTH = 270
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the road image
roadImage = pygame.image.load("road.png").convert()
car = pygame.image.load('carTop.png')

# Rotate the road image by 90 degrees
roadImage = pygame.transform.rotate(roadImage, -90)

#resize car
car = pygame.transform.scale(car, [70, 120])

# Resize the road image to fit the screen height
roadImage = pygame.transform.scale(roadImage, (roadImage.get_width(), SCREEN_HEIGHT))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Set the initial position of the road image
roadPos = 0

carPosx = 97
carPosy = 400
carXspeed = 2
carYspeedBack = 1.2
carYspeedUp = .5
carSlowingSpeed = 0
carSpeedingSpeed = 0

spark = pygame.image.load('sparks.png')
spark = pygame.transform.scale(spark, [40, 50])



# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    

    # Scroll the road image
    roadPos += 3
    if roadPos > SCREEN_HEIGHT:
        roadPos = 0


    carPosy -= .08
    carPosy -= carSpeedingSpeed
    keys = pygame.key.get_pressed()
    
    # Check for player movement
    if keys[pygame.K_DOWN]:
        carPosy += carYspeedBack
        carSlowingSpeed += .005
        carPosy += carSlowingSpeed
        carSpeedingSpeed = 0
    if keys[pygame.K_UP]:
        carPosy -= carYspeedUp
        carSpeedingSpeed += 0.005
        carPosy -= carSpeedingSpeed
        carSlowingSpeed = 0
    if keys[pygame.K_LEFT]:
        carPosx -= carXspeed
    if keys[pygame.K_RIGHT]:
        carPosx += carXspeed


    if carPosx < 10:
        carPosx += carXspeed


    if carPosx > 185:
        screen.blit(spark, (carPosx + 20, carPosy - 10))
        carPosx -= carXspeed


    # Draw the road image
    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
    screen.blit(roadImage, (0, roadPos))

    screen.blit(car, (carPosx, carPosy))

    

    

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
