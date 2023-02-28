import pygame
import os
import sys
import random
pygame.init()

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

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

obstacle1 = pygame.image.load('obstacleCar1.png')
obstacle1 = pygame.transform.scale(obstacle1, [70, 120])
obstacle1 = pygame.transform.rotate(obstacle1, 0)
obstacle1R = obstacle1.get_rect()

obstacle2 = pygame.image.load('obstacleCar2.png')
obstacle2 = pygame.transform.rotate(obstacle2, 90)
obstacle2 = pygame.transform.scale(obstacle2, [70, 120])
obstacle2 = pygame.transform.rotate(obstacle2, -90)
obstacle2R = obstacle2.get_rect()

obstacle3 = pygame.image.load('obstacleCar3.png')
obstacle3 = pygame.transform.scale(obstacle3, [70, 120])
obstacle3 = pygame.transform.rotate(obstacle3, 0)
obstacle3 = obstacle3.get_rect()

obstacle4 = pygame.image.load('obstacleCar4.png')
obstacle4 = pygame.transform.scale(obstacle4, [70, 120])
obstacle4 = pygame.transform.rotate(obstacle4, 0)
obstacle4 = obstacle4.get_rect()

obstacle5 = pygame.image.load('obstacleCar5.png')
obstacle5 = pygame.transform.scale(obstacle5, [70, 120])
obstacle5 = pygame.transform.rotate(obstacle5, 90)
obstacle5 = obstacle5.get_rect()

# Resize the road image to fit the screen height
roadImage = pygame.transform.scale(roadImage, (roadImage.get_width(), SCREEN_HEIGHT))

# Create a clock to control the frame rate
clock = pygame.time.Clock()


counting = False
drifting1 = False
currentCountPoint = 0
numb = 0
driftTime = 0
obstacles = ["obstacle1", "obstacle2"]
lanes = [10, 100, 190]
possibleObstacleSpeeds = [0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4]
# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
    screen.blit(roadImage, (0, roadPos))

    screen.blit(car, (carPosx, carPosy))

    

    # Scroll the road image
    roadPos += roadSpeed
    if roadPos > SCREEN_HEIGHT:
        roadPos = 0


    if obstacle1R0.colliderect(obstacle2R0):
        if obstacle1posy <= obstacle2posy:
            speedObstacle1 = speedObstacle2 + 2
        elif obstacle1posy >= obstacle2posy:
            speedObstacle1 = speedObstacle2 - 2



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
        if roadSpeed > 7:
            roadSpeed -= .01
        if carXspeed > 2.5:
            carXspeed -= .01
        carXspeed += .01
    if keys[pygame.K_LEFT]:
        carPosx -= carXspeed
    if keys[pygame.K_RIGHT]:
        carPosx += carXspeed
    elif carIsRotated is True:
        carIsRotated = False
        car = pygame.image.load('carTop.png')
        car = pygame.transform.scale(car, [70, 120])
        car = pygame.transform.rotate(car, 0)


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