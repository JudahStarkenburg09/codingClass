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
obstacle1posy = -200
speedObstacle1 = 1
obstacle1OnScreen = False
obstacle1R = obstacle1.get_rect()

obstacle2 = pygame.image.load('obstacleCar2.png')
obstacle2 = pygame.transform.rotate(obstacle2, 90)
obstacle2 = pygame.transform.scale(obstacle2, [70, 120])
obstacle2posy = -200
speedObstacle2 = 1
obstacle2OnScreen = False
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


    roadSpeed += 0.0001

    # Draw the images
    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
    screen.blit(roadImage, (0, roadPos))
    screen.blit(car, (carPosx, carPosy))

    carRect = pygame.Rect(carPosx, carPosy, car.get_width(), car.get_height())

    #Obstacle Does Bad Driving:
    if counting == False:
        counting = True
        currentCountPoint = 0
        countTo = random.randint(1000, 2000)
    if counting == True:
        print("counting to: " + str(countTo))
        print("at: " + str(currentCountPoint))
        currentCountPoint += 1
        if currentCountPoint == countTo:
            #set to the amount of obstacles -v
            selectedDrunk = random.randint(1,2)
            #left = 1, right = 2
            selectedDrift = random.randint(1,2)
            if selectedDrunk == 1:
                if selectedDrift == 1:
                    drifting1 = True

    if drifting1 == True:
        driftTime += 1
        laneChosen1 += 2
        counting == False
    if driftTime == 10:
        driftTime == 0
        drifting1 = False




    #obstacle1
    if obstacle1OnScreen == False:
        obstacle1OnScreen = True
    
    if obstacle1OnScreen == True:
        if obstacle1posy == -200:
            laneChosen1 = random.choice(lanes)
            speedObstacle1 = random.choice(possibleObstacleSpeeds)
        screen.blit(obstacle1, (laneChosen1, obstacle1posy))
        obstacle1R = obstacle1.get_rect(left=(laneChosen1 + 15), top=(obstacle1posy + 15), width=(obstacle1.get_width() - 30), height=(obstacle1.get_height() - 30))
        obstacle1R0 = obstacle1.get_rect(left=laneChosen1, top=obstacle1posy, width=obstacle1.get_width(), height=obstacle1.get_height())
        obstacle1posy += roadSpeed - speedObstacle1

    if obstacle1posy > 750:
        obstacle1OnScreen = False
        obstacle1posy = -200

    #obstacle2
    if obstacle2OnScreen == False:
        obstacle2OnScreen = True
    
    if obstacle2OnScreen == True:
        if obstacle2posy == -200:
            laneChosen2 = random.choice(lanes)
            speedObstacle2 = random.choice(possibleObstacleSpeeds)
        screen.blit(obstacle2, (laneChosen2, obstacle2posy))
        obstacle2R = obstacle2.get_rect(left=(laneChosen2 + 15), top=(obstacle2posy + 15), width=(obstacle2.get_width() - 30), height=(obstacle2.get_height() - 30))
        obstacle2R0 = obstacle2.get_rect(left=laneChosen2, top=obstacle2posy, width=obstacle2.get_width(), height=obstacle2.get_height())
        obstacle2posy += roadSpeed - speedObstacle2 

    if obstacle2posy > 750:
        obstacle2OnScreen = False
        obstacle2posy = -200
    
    
    if carRect.colliderect(obstacle1R):
        numb += 1
        print('crash' + str(numb))

    if carRect.colliderect(obstacle2R):
        numb += 1 
        print('crash' + str(numb))

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
        if carIsRotated is not True:
            car = pygame.image.load('carTop.png')
            car = pygame.transform.scale(car, [70, 120])
            car = pygame.transform.rotate(car, 4)
            carIsRotated = True
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