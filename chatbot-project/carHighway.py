import pygame
import os
import sys
import random
pygame.init()

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

# Set up the screen
SCREEN_WIDTH = 270
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the road image
roadImage = pygame.image.load("road.png").convert()
car = pygame.image.load('carTop.png')
car = pygame.transform.scale(car, [70, 120])
car = pygame.transform.rotate(car, 0)

# Rotate the road image by 90 degrees
roadImage = pygame.transform.rotate(roadImage, -90)

obstacle1 = pygame.image.load('obstacleCar1.png')
obstacle1 = pygame.transform.scale(obstacle1, [70, 120])
obstacle1 = pygame.transform.rotate(obstacle1, 0)
obstacle1R = obstacle1.get_rect()

obstacle2 = pygame.image.load('obstacleCar2.png')
obstacle2 = pygame.transform.scale(obstacle2, [70, 120])
obstacle2 = pygame.transform.rotate(obstacle2, -90)
obstacle2R = obstacle2.get_rect()

obstacle3 = pygame.image.load('obstacleCar3.png')
obstacle3 = pygame.transform.scale(obstacle3, [70, 120])
obstacle3 = pygame.transform.rotate(obstacle3, 0)
obstacle3R = obstacle3.get_rect()

obstacle4 = pygame.image.load('obstacleCar4.png')
obstacle4 = pygame.transform.scale(obstacle4, [70, 120])
obstacle4 = pygame.transform.rotate(obstacle4, 0)
obstacle4R = obstacle4.get_rect()

obstacle5 = pygame.image.load('obstacleCar5.png')
obstacle5 = pygame.transform.scale(obstacle5, [70, 120])
obstacle5 = pygame.transform.rotate(obstacle5, 90)
obstacle5R = obstacle5.get_rect()

# Resize the road image to fit the screen height
roadImage = pygame.transform.scale(roadImage, (roadImage.get_width(), SCREEN_HEIGHT))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Set the initial position of the road image
roadPos = 0

carPosx = 100
carPosy = 400
carXspeed = 2
carYspeedBack = 1.2
carYspeedUp = .5
carSlowingSpeed = 0
carSpeedingSpeed = 0
carIsRotated = False
roadSpeed = 3.5
spark = pygame.image.load('sparks.png')
spark = pygame.transform.scale(spark, [100, 100])

lanes = [10, 100, 190]

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # Draw the images
    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
    screen.blit(roadImage, (0, roadPos))
    screen.blit(car, (carPosx, carPosy))


    # Scroll the road image
    roadPos += roadSpeed
    if roadPos > SCREEN_HEIGHT:
        roadPos = 0


    keys = pygame.key.get_pressed()
    
    # Check for player movement
    if keys[pygame.K_DOWN]:
        roadSpeed -= .01
        if roadSpeed < 2:
            roadSpeed += .01
        if carXspeed < 1.5:
            carXspeed += .01
        carXspeed -= .01
    if keys[pygame.K_UP]:
        roadSpeed += .01
        if roadSpeed > 5:
            roadSpeed -= .01
        if carXspeed > 2.5:
            carXspeed -= .01
        carXspeed += .01
    if keys[pygame.K_LEFT]:
        if carIsRotated is not True:
            car = pygame.image.load('carTop.png')
            car = pygame.transform.scale(car, [70, 120])
            car = pygame.transform.rotate(car, 4)
            carIsRotated = True
        if carIsRotated is True and carPosx == 11:
            ()
        carPosx -= carXspeed
            
    elif keys[pygame.K_RIGHT]:
        if carIsRotated is not True:
            car = pygame.image.load('carTop.png')
            car = pygame.transform.scale(car, [70, 120])
            car = pygame.transform.rotate(car, -4)
            carIsRotated = True
        carPosx += carXspeed
    elif carIsRotated is True:
        carIsRotated = False
        car = pygame.image.load('carTop.png')
        car = pygame.transform.scale(car, [70, 120])
        car = pygame.transform.rotate(car, 0)


    if carPosx < 10:
        screen.blit(spark, (carPosx - 60, carPosy - 30))
        carPosx += carXspeed


    if carPosx > 185:
        screen.blit(spark, (carPosx + 20, carPosy - 30))
        carPosx -= carXspeed



    

    

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)