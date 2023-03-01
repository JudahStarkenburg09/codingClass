# current_directory = os.getcwd()
# folder1 = 'data'
# os.chdir(os.path.join(current_directory, folder1))
def carGame():    
    import pygame
    import os
    import sys
    import random
    pygame.init()


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
    maxSpeed = 5
    minSpeed = 3


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

    obstacle3 = pygame.image.load('obstacleCar5.png')
    obstacle3 = pygame.transform.rotate(obstacle3, -90)
    obstacle3 = pygame.transform.scale(obstacle3, [70, 120])
    obstacle3posy = -200
    speedObstacle3 = 1
    obstacle3OnScreen = False
    obstacle3R = obstacle3.get_rect()

    obstacle4 = pygame.image.load('obstacleCar4.png')
    obstacle4 = pygame.transform.scale(obstacle4, [70, 120])
    obstacle4 = pygame.transform.rotate(obstacle4, 0)
    obstacle4R = obstacle4.get_rect()

    obstacle5 = pygame.image.load('obstacleCar5.png')
    obstacle5 = pygame.transform.scale(obstacle5, [70, 120])
    obstacle5 = pygame.transform.rotate(obstacle5, 90)
    obstacle5R = obstacle5.get_rect()

    obstacle7 = pygame.image.load('obstacleCar4.png')
    obstacle7 = pygame.transform.rotate(obstacle7, 0)
    obstacle7 = pygame.transform.scale(obstacle7, [70, 120])
    obstacle7posy = -200
    speedObstacle7 = 1
    obstacle7OnScreen = False
    obstacle7R = obstacle7.get_rect()

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
    possibleObstacleSpeeds = [2.4, 2.6, 2.8, 3, 3.2, 3.4]
    dangerSpeed = 0
    boostCharge = 10
    level1 = 1000
    level2 = 1000
    level3 = 1000
    levelCountdown = level1
    onLevel = 'level1'
    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'game done'
                sys.exit()


        # Draw the images
        screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
        screen.blit(roadImage, (0, roadPos))
        screen.blit(car, (carPosx, carPosy))

        carRect = pygame.Rect(carPosx, carPosy, car.get_width(), car.get_height())

        # print(onLevel + ' --> ' + str(levelCountdown) + ', Current Speed Is ' + str(roadSpeed) + '. || Min Speed Is ' + str(minSpeed) + '. || Max Speed Is ' + str(maxSpeed)) #THIS LINE IS FOR TESTING
        if onLevel == 'level1':
            level1 -= 1
            levelCountdown = str(level1)
            if level1 <= 0:
                maxSpeed = 6
                minSpeed = 4
                onLevel = 'level2'
        if onLevel == 'level2':
            level2 -= 1
            levelCountdown = str(level2)
            if level2 <= 0:
                maxSpeed = 7
                minSpeed = 5
                onLevel = 'level3'



        #obstacle1
        if obstacle1OnScreen == False:
            obstacle1OnScreen = True
        
        if obstacle1OnScreen == True:
            if obstacle1posy == -200:
                laneChosen1 = random.choice(lanes)
                speedObstacle1 = random.choice(possibleObstacleSpeeds)
            screen.blit(obstacle1, (laneChosen1, obstacle1posy))
            obstacle1R = obstacle1.get_rect(left=(laneChosen1 + 15), top=(obstacle1posy + 17), width=(obstacle1.get_width() - 30), height=(obstacle1.get_height() - 30))
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
            obstacle2R = obstacle2.get_rect(left=(laneChosen2 + 15), top=(obstacle2posy + 17), width=(obstacle2.get_width() - 30), height=(obstacle2.get_height() - 30))
            obstacle2R0 = obstacle2.get_rect(left=laneChosen2, top=obstacle2posy, width=obstacle2.get_width(), height=obstacle2.get_height())
            obstacle2posy += roadSpeed - speedObstacle2 

        if obstacle2posy > 750:
            obstacle2OnScreen = False
            obstacle2posy = -200
        
        #obstacle3
        if obstacle3OnScreen == False:
            obstacle3OnScreen = True
        
        if obstacle3OnScreen == True:
            if obstacle3posy == -200:
                laneChosen3 = random.choice(lanes)
                speedObstacle3 = random.choice(possibleObstacleSpeeds)
            screen.blit(obstacle3, (laneChosen3, obstacle3posy))
            obstacle3R = obstacle3.get_rect(left=(laneChosen3 + 15), top=(obstacle3posy + 17), width=(obstacle3.get_width() - 30), height=(obstacle3.get_height() - 30))
            obstacle3R0 = obstacle3.get_rect(left=laneChosen3, top=obstacle3posy, width=obstacle3.get_width(), height=obstacle3.get_height())
            obstacle3posy += roadSpeed - speedObstacle3

        if obstacle3posy > 750:
            obstacle3OnScreen = False
            obstacle3posy = -200

        #obstacle7
        if obstacle7OnScreen == False:
            obstacle7OnScreen = True
        
        if obstacle7OnScreen == True:
            if obstacle7posy == -200:
                laneChosen7 = random.choice(lanes)
                speedobstacle7 = random.choice(possibleObstacleSpeeds)
            screen.blit(obstacle7, (laneChosen7, obstacle7posy))
            obstacle7R = obstacle7.get_rect(left=(laneChosen7 + 15), top=(obstacle7posy + 17), width=(obstacle7.get_width() - 30), height=(obstacle7.get_height() - 30))
            obstacle7R0 = obstacle7.get_rect(left=laneChosen7, top=obstacle7posy, width=obstacle7.get_width(), height=obstacle7.get_height())
            obstacle7posy += roadSpeed - speedobstacle7

        if obstacle7posy > 750:
            obstacle7OnScreen = False
            obstacle7posy = -200
        
        
        if carRect.colliderect(obstacle1R):
            numb += 1
            print('crash' + str(numb))

        if carRect.colliderect(obstacle2R):
            numb += 1 
            print('crash' + str(numb))

        if carRect.colliderect(obstacle3R):
            numb += 1 
            print('crash' + str(numb))

        # Scroll the road image
        roadPos += roadSpeed
        if roadPos > SCREEN_HEIGHT:
            roadPos = 0

        #collisions with other cars
        if obstacle1R0.colliderect(obstacle2R0):
            if obstacle1posy <= obstacle2posy:
                speedObstacle1 = speedObstacle2 + 2
            elif obstacle1posy >= obstacle2posy:
                speedObstacle1 = speedObstacle2 - 2
        if obstacle2R0.colliderect(obstacle3R0):
            if obstacle2posy <= obstacle3posy:
                speedObstacle2 = speedObstacle3 + 2
            elif obstacle2posy >= obstacle3posy:
                speedObstacle2 = speedObstacle3 - 2
        if obstacle1R0.colliderect(obstacle3R0):
            if obstacle1posy <= obstacle3posy:
                speedObstacle1 = speedObstacle3 + 2
            elif obstacle1posy >= obstacle3posy:
                speedObstacle1 = speedObstacle3 - 2
        if obstacle1R0.colliderect(obstacle7R0):
            if obstacle1posy <= obstacle7posy:
                speedObstacle1 = speedObstacle7 + 2
            elif obstacle1posy >= obstacle7posy:
                speedObstacle1 = speedObstacle7 - 2
        if obstacle2R0.colliderect(obstacle7R0):
            if obstacle2posy <= obstacle7posy:
                speedObstacle1 = speedObstacle7 + 2
            elif obstacle2posy >= obstacle7posy:
                speedObstacle2 = speedObstacle7 - 2
        if obstacle3R0.colliderect(obstacle7R0):
            if obstacle3posy <= obstacle7posy:
                speedObstacle3 = speedObstacle7 + 2
            elif obstacle3posy >= obstacle7posy:
                speedObstacle3 = speedObstacle7 - 2


        if roadSpeed < minSpeed:
            roadSpeed += .08
        if roadSpeed > maxSpeed:
            roadSpeed -= .03
        keys = pygame.key.get_pressed()
        
        # Check for player movement
        if keys[pygame.K_DOWN]:
            roadSpeed -= .07

            if carXspeed < 1.5:
                carXspeed += .07
            carXspeed -= .01
        if keys[pygame.K_UP]:
            roadSpeed += .03
            if carXspeed > 2.5:
                carXspeed -= .03
            carXspeed += .01
            dangerSpeed += 0.001
            
            
            if dangerSpeed >= 1:
                if boostCharge > 0:
                    roadSpeed = maxSpeed + 2
                    #PUT HERE WHAT HAPPENS AT DANGERSPEED
                else:
                    dangerSpeed = 0
                    boostCharge = 10
                    if roadSpeed > maxSpeed:
                        roadSpeed -= 0.1

                boostCharge -= 0.01
        else:
            dangerSpeed = 0
            if roadSpeed > maxSpeed:
                roadSpeed -= 0.1
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