import pygame
import os
import sys
import random
import json



credentialsForLinusCo = [
    {
    "type": "service_account",
    "project_id": "linus-co",
    "private_key_id": "0b022dbad08459c7dcf87f4867011c90ed2b3bc1",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDCwjyOd8haRZEK\nGQCPDRnGAl2z2H085F1nOirCYvT9wd1uA8l5NO4hTedxV6glpiV6GdpjNoeR85Ab\n100LmfDxJyeOdCKlWoXKvT0iQb0IC2V7qtkCQigzP/mAR2FeELM0Rlbgfog2O1qy\nVTdZ/8WrYj1xkgRrcCbZTM3UVa+CTwX552kynwV5l55XUAZ38tlm841Q/tdLGiYm\nJOB/B7lqh4Rcl0Cyj69ppQG9mmIlhFntB3GgF0cgwsrtAbHWM4rIArNS5oZ2d6EE\npwkcQ4h5LoWBbtiGOXlKtNVU9IlfYDTaNjtoDXrs9U0k3NkQVv6ulVZMR/aHXePQ\nwMx+0MLbAgMBAAECggEAOuqKaijHNbO8xBq7Jgs3BET79qdjf3Ov48XfYI2SAl/O\nrfS8UovWC8Im5Q044ybHSJAglgnNajQNoLZ5aqyHjFQlbb0pK+9d8O5dW4sadaAI\n86fD3SCJS7OrNQii5lNT+tjaeDAe4ZUEA1WvGG087XMbFkuvRZcYUX0f+P9wyBC7\no9h9cPCvcpnLEZv0fNYqa7rgWeHV8iLoSB/gR3svMk1giT/DNxAVzhMpuldEKmbx\nYrS5cc+N+a/zQS/rym6ZfeVnsycGaJ9gvHe0nPgRlzF3izJX6wigjJlxa8WP26Rg\nofhC3Xv8u0Bk3Squ96A9/BH6MoJ5qg+qRDiW/2VFLQKBgQDkMGl+YJW3UPcCGS3f\nHdYYgMSiBNFB2/JUYdbd0J4N86W24jsX2iyEeNTDf+zC02XtRdl5kxJHFv5s2Tqp\nat6LmLy3nDKUMZ0I0Afw9xXCqifvtco1gtt+WwQAGtwSl/b3wZFWjYPh8t9c3Hhv\nNorbEh4v6X26WcJFqUJ/OVvqzQKBgQDafsiyfw7VWBkBfFcBBgDzAGsALjLrO5WS\nVuMiM/S8o24F+cc+popl6s2SoAi28uL1OM6iABtcdsA6z52fTJagXE6/7WQ/pWyK\nsCAY5FQ9HkoTmfg0vz7q8OeWu7uCsDDqoasP19wqMIsRYI0cyluNWvxdzqWwoxHz\nn+mJ5yU0RwKBgQDI4nHMxvymsIlz+HSwqlSTp7DzrWgHIbl5XdTJ2+F5CNkHYqyB\nOBne2Xz9Sv5FGdPuiYKGC9qYaP69FpQVF7cpj+H7hm/klLTZUELdeLhYcnHMDu8g\nIr5Ww4uHCB5b5BqQTIFFgDntTWIkHxeLWKnvaEjZByYfSuvDZdnbpMRttQKBgAXR\nVGS0T1/M3bWVavejAkl2HGM/16k9x+jCmX+ipISVUWulT/HSG2NFUj3yNukwJGzl\nG1Ni71eR7eJi/s5sCqKwcoRXvNCZBf/XWrNu+PM7qDtHYT1+Th2RVolD7GU5bcQB\nk/1zAPC6pClNSdSXasKjxo503yKJ5QN4oY5DclEnAoGBAKE7k7cQgKuGstcL+Gpa\nXG+1+5pKqewcBfhjzTjpFXRDYHJA27IqvI/9liQvLb8N9XMgpMIv8L2xTwCObPOD\nA16HRwqPkfXFZZu0nzGaJMza9ihptdrzp81dnSGJ+wvHWtlVadwHJxwth3hDxq2E\n/bhN9SDdHIRbU4Os2d5O+AvE\n-----END PRIVATE KEY-----\n",
    "client_email": "linus-cooperation@linus-co.iam.gserviceaccount.com",
    "client_id": "113135078032571665296",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/linus-cooperation%40linus-co.iam.gserviceaccount.com"
    }
]


credsDataLinus = json.load(credentialsForLinusCo)

pygame.init()


current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))




def playAgain():
    print("playing Again")

def menu():
    button_rect = pygame.Rect(70, 260, 130, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button was clicked
                if button_rect.collidepoint(event.pos):
                    playAgain()
        screen.blit(roadImage, (0, roadPos))
        screen.blit(car, (carPosx, carPosy))
        screen.blit(obstacle3, (laneChosen3, obstacle3posy))
        screen.blit(obstacle1, (laneChosen1, obstacle1posy))
        screen.blit(obstacle2, (laneChosen2, obstacle2posy))
        scoreBGWidth, scoreBGHeight = 64, 28  # Update the dimensions of the surface
        rect_surface = pygame.Surface((scoreBGWidth, scoreBGHeight), pygame.SRCALPHA)
        rect_surface.set_alpha(200)
        pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, scoreBGWidth, scoreBGHeight)) 
        screen.blit(rect_surface, (195, 5))  # Update the position where the surface is blitted
        screen.blit(scoreText, (200, 10))

        menuX, menuY = 230, 350  # Update the dimensions of the surface
        rect_surface = pygame.Surface((menuX, menuY), pygame.SRCALPHA)
        rect_surface.set_alpha(200)
        pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, menuX, menuY))  # Draw a rectangle at (0, 0) with dimensions of the surface
        screen.blit(rect_surface, (20, 80))  # Update the position where the surface is blitted
        scoreXY = (130, 230)

        text1 = font.render(f'Final Score Is', True, (255, 255, 255))
        text2 = font.render(f'{score}', True, (255, 255, 255))
        text2_width = text2.get_width()  # Get the width of the second text surface
        if int(len(str(text2))) > 1:
            scoreXY = (130 - text2_width // 2, 230)  # Center the second text surface in the rectangle
        screen.blit(text1, (70, 200))
        screen.blit(text2, scoreXY)

        # Set up the first button
        # Draw the button
        pygame.draw.rect(screen, (50, 50, 255), button_rect)

        # Add text to the button
        text = font.render("Play Again", True, (245, 255, 245))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)



        pygame.display.update()  # update the screen 
        pygame.display.flip()    

        clock.tick(60)


def lose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))

    scoreBGWidth, scoreBGHeight = 64, 28  # Update the dimensions of the surface
    rect_surface = pygame.Surface((scoreBGWidth, scoreBGHeight), pygame.SRCALPHA)
    rect_surface.set_alpha(200)
    pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, scoreBGWidth, scoreBGHeight))  # Draw a rectangle at (0, 0) with dimensions of the surface
    screen.blit(rect_surface, (195, 5))  # Update the position where the surface is blitted
    
    screen.blit(roadImage, (0, roadPos))
    screen.blit(car, (carPosx, carPosy))
    screen.blit(obstacle3, (laneChosen3, obstacle3posy))
    screen.blit(obstacle1, (laneChosen1, obstacle1posy))
    screen.blit(obstacle2, (laneChosen2, obstacle2posy))
    screen.blit(scoreText, (200, 10))
    pygame.display.update()  # update the screen 
    pygame.display.flip()
    clock.tick(2000)
    menu()



gameRun = True
def crash():
    global gameRun
    gameRun = False
    for i in range(7):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
        screen.blit(roadImage, (0, roadPos))
        screen.blit(car, (carPosx, carPosy))
        screen.blit(obstacle3, (laneChosen3, obstacle3posy))
        screen.blit(obstacle1, (laneChosen1, obstacle1posy))
        screen.blit(obstacle2, (laneChosen2, obstacle2posy))
        screen.blit(scoreText, (200, 10))

        scoreBGWidth, scoreBGHeight = 64, 28  # Update the dimensions of the surface
        rect_surface = pygame.Surface((scoreBGWidth, scoreBGHeight), pygame.SRCALPHA)
        rect_surface.set_alpha(200)
        pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, scoreBGWidth, scoreBGHeight))  # Draw a rectangle at (0, 0) with dimensions of the surface
        screen.blit(rect_surface, (195, 5))  # Update the position where the surface is blitted

        animatedImage = pygame.image.load((images[i])["image"])
        screen.blit(animatedImage, ((images[i]))["location"])
        
        pygame.display.update()  # update the screen 
        pygame.display.flip()
        pygame.time.delay(70)  # pause for 70 milliseconds (0.07 seconds)



    
    lose()
    





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
minSpeed = 2.6


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
obstacle3 = pygame.transform.rotate(obstacle3, -90)
obstacle3 = pygame.transform.scale(obstacle3, [70, 120])
obstacle3posy = -200
speedObstacle3 = 1
obstacle3OnScreen = False
obstacle3R = obstacle3.get_rect()


# Resize the road image to fit the screen height
roadImage = pygame.transform.scale(roadImage, (roadImage.get_width(), SCREEN_HEIGHT))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
counting = False
drifting1 = False
currentCountPoint = 0
numb = 0
driftTime = 0
obstacles = ["obstacle1", "obstacle2", "obstacle3"]
lanes = [10, 100, 190]
possibleObstacleSpeeds = [2.4, 2.6, 2.8, 3, 3.2, 3.4]
dangerSpeed = 0
boostCharge = 10
level1 = 1000
level2 = 1000
level3 = 1000
levelCountdown = level1
onLevel = 'level1'

score = 0

scoreWait = 0
# Main game loop
while True and gameRun == True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    animateLocation = [carPosx - 50, carPosy - 20]

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





    #how fast score counts
    scoreWait = scoreWait + (roadSpeed/5)
    if scoreWait >= 30:
        scoreWait = 0
        score = score + 1
    scoreText = font.render(str(score), True, (255, 255, 255))
    # Draw the images
    screen.blit(roadImage, (0, roadPos - SCREEN_HEIGHT))
    screen.blit(roadImage, (0, roadPos))
    screen.blit(car, (carPosx, carPosy))

    carRect = pygame.Rect(carPosx, carPosy, car.get_width(), car.get_height())

    # print(onLevel + ' --> ' + str(levelCountdown) + ', Current Speed Is ' + str(roadSpeed) + '. || Min Speed Is ' + str(minSpeed) + '. || Max Speed Is ' + str(maxSpeed))
    if onLevel == 'level1':
        level1 -= 1
        levelCountdown = str(level1)
        if level1 <= 0:
            maxSpeed = 6
            minSpeed = 3
            onLevel = 'level2'
    if onLevel == 'level2':
        level2 -= 1
        levelCountdown = str(level2)
        if level2 <= 0:
            maxSpeed = 7
            minSpeed = 3.4
            onLevel = 'level3'
    if onLevel == 'level3':
        level3 = 'Last Level (Infinite)'
        levelCountdown = str(level3)
        minSpeed += 0.00037037037037037035
        maxSpeed += 0.00037037037037037035



    #obstacle1
    if obstacle1OnScreen == False:
        obstacle1OnScreen = True
    
    if obstacle1posy < -200:
        speedObstacle1 = roadSpeed - .4

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

    if obstacle2posy < -200:
        speedObstacle2 = roadSpeed - .4
    
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

    if obstacle3posy < -200:
        speedObstacle3 = roadSpeed - .4
    
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

    
    
    if carRect.colliderect(obstacle1R):
        crash()

    if carRect.colliderect(obstacle2R):
        crash()

    if carRect.colliderect(obstacle3R):
        crash()

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


            


    if roadSpeed < minSpeed:
        roadSpeed = minSpeed
    if roadSpeed > maxSpeed:
        roadSpeed = maxSpeed
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



    scoreBGWidth, scoreBGHeight = 64, 28  # Update the dimensions of the surface
    rect_surface = pygame.Surface((scoreBGWidth, scoreBGHeight), pygame.SRCALPHA)
    rect_surface.set_alpha(200)
    pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, scoreBGWidth, scoreBGHeight))  # Draw a rectangle at (0, 0) with dimensions of the surface
    screen.blit(rect_surface, (195, 5))  # Update the position where the surface is blitted

    screen.blit(scoreText, (200, 10))
    

    
    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)