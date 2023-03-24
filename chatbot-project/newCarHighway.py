import pygame
import os
import sys
import random
import pygsheets
import json
import tkinter as tk
from tkinter import messagebox

def login_menu():
    global playAgain
    # Create the main window
    window = tk.Tk()
    window.title("Login Menu")
    icon = tk.PhotoImage(file="CarHighwayLogo.ico")

    # Set the iconphoto attribute of the window to the photo image object
    window.iconphoto(False, icon)

    # Create the username label
    username_label = tk.Label(window, text="Use the same username every time if you have played this game before!")
    username_label.pack()

    # Create the username input box
    username_var = tk.StringVar()   
    username_entry = tk.Entry(window, textvariable=username_var)
    username_entry.pack()

    # Define the submit function
    def submit():
        global user
        if len(username_var.get()) > 8:
            tk.messagebox.showerror("Error", "Username must be 8 characters or less")
        else:
            user = username_var.get()
            window.destroy()

    # Create the submit button and bind it to the Enter key
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()
    window.bind('<Return>', lambda event: submit())

    # Handle window close event
    def on_closing():
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            global playAgain
            window.destroy()
            playAgain = False
            exit()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main event loop
    window.mainloop()






current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))  
errorTest = 0

pygame.init()

newHighScore = None
# add credentials to the account
creds = json.dumps({
    "type": "service_account",
    "project_id": "linus-co",
    "private_key_id": "5f8ac6ad7e2535d14626e3eeeca3aec93ce19614",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvBNFv/7FitDdt\nbTpLaDjmuDTQSOHqjwAk98zQCktx3CXh+n0DXXtYMN1+PdsvkwiCPdhtcwaguStV\naQucji5L0C9stgpKPSUcuEJAdwEgHj9mbbb1NgM4s+meKFJFOG69F17LOE3scRiA\nqif79pR4Omtx6gmLai/1Z3hhAD6k9YKmicBY2h/Dl7sk12LHHSifLEHaWmCLxdkl\n9p3KNUjvY8+0BYd7SxTe6bk7Lf8vbCTDBg3jn5/hRgTbmF7coSk9fX5KLE6klFDJ\n3FmHSV5BnNn0Czffr71X5miYeSI2EHStp23azNLKU6JYMnQWwwyaRkR9q5N026ic\nNH1xlsPvAgMBAAECggEADP6slkZD43JCE0vi4ipw3yCaO0TOEV5gwl3rxR6ej2ur\nHGY+1fsg52FpcLAjEBs4rILvCOFbgp99CjBsfklIQrTIcKfrh6uWj9VWhfbQDJRy\nXKaUyQwjnRgupmGUCjOwdTXBAhHCJ2YWTadUpK6gQ3UC+UhJQSK3QN9X3svn2tOI\nWaTLdwR0zQYkwO5UaKm/kx5gYh8/uSI+l100fSC3osX5vFfB16LzGwX9LGVd15Bi\nnqmptj5/OHaSCDkU6mZfHNHyZtpNeA0QIK1CDxIw99r3/+7HPk7mCAUM3kriCbsx\n4NAo0dOhpgL8pUTFeX3APJ/2uvVvdySVOEKhpTH40QKBgQDXoRTuPC21HT298d1K\n+Iw7TR1u1a8+iYNM4ud/2t2bal/bDb4en5a8wHXZut7BGohgVq3VF+zs1d9Y1C4X\nK+bbmRe8FOb9rwbGeGyysJtdXQsuRmWVOzomfV5PPMJXJg9RosbuIVukEgdoFmT8\nh9bIHfYBDTGYWUykD1wrqx6WVQKBgQDPyVDG9/S2VIvFD3X4tv0UoI30xIDyo8Yx\nRHAIPfvH2fLHLYNgDTir+wqJnxxNtd075dvVDVgiGzHuRpf9pI9LQ7/5Fz78cvJv\n0P62SeHf9OGlNmRWTQOeRqQKc5yuaQ+Skz1tarbCrYgrF4juBabWMgSJ/k3fFrdM\nRApouOqNMwKBgGzgLdRY2G9hs2IsNKN9OjlbJ6hmBtVZ081HqMJa/ZhSrtHJb5zA\n0fi+aQMmIwF35zJVsfIt4Xh4SQzuHdOfXDK3a0+RckzXSmF+Psw+9kO/Dj0wWGxw\nel0i4jK6KBqe4g9DVJS6jS4b2FeLLzR/Vki3MBa51bfqJxOTmeOGxKv9AoGAZ1y0\nsxV7hQvPr4p+W+fjQ1SO6TirEIiJuc5akK8MxaDUlWI9nRVWoK6z0jv1H28di4NP\ndM87jVPL5cT2LLWkloMwRx/aNEiV8yua2WEtXHP7n2zMQuXyq9RmG9DhGx2mInre\nLsTL/1HFj/IYKpdjI+Ajw+VeJWCuc+DQ8MEz5GMCgYBDMluUqOcRxpHMnXK4g2Ln\nmuyfeih/KhOBQxRWWNvsF7JQ2g+cY+g6yAYt9cRVFXItfkVONSJn58JfBozimEmI\nYffEPg+BVccOS4bf5TqD+bBcAX5GXpq5avat9CZqNbgOKtj2QmlNb7/dGXBZEo2v\noV5xDw7qLdmxY/K+A9mZCg==\n-----END PRIVATE KEY-----\n",
    "client_email": "linus-co-op@linus-co.iam.gserviceaccount.com",
    "client_id": "110264289236205928194",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/linus-co-op%40linus-co.iam.gserviceaccount.com"
    })
# set up credentials
gc = pygsheets.authorize(service_account_json=creds)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1nWb4ZTeLfldXi_7kQ--qB65GLoX7JB_k5YzAIKiPocA/edit#gid=0'
sh = gc.open_by_url(sheet_url)

worksheet = sh[0]

login_menu()

roadPos = 0
gameJustStarted = True
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
# images
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
# variables
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
gameRun = True
errorWithGame = False



# notificationBox = pygame.
# textOnNotification = 

#region Functions ----------
def initVariables():
    global score, roadSpeed, maxSpeed, minSpeed, level1, level2, level3, levelCountdown, numb, onLevel, roadPos, carPosx, carPosy, carIsRotated, gameRun, obstacle3OnScreen, obstacle2OnScreen, obstacle1OnScreen, laneChosen1, laneChosen3, laneChosen2, images, scoreText, scoreWait, car, carPosx, carPosy, obstacle1posy, obstacle2posy, obstacle3posy, speedObstacle1, speedObstacle2, speedObstacle3, carXspeed, errorWithGame, gameJustStarted
    errorWithGame = False
    gameJustStarted = True
    roadPos = 0
    carPosx = 100
    carPosy = 400
    carXspeed = 2
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
    # images
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
    # variables
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    numb = 0
    level1 = 1000
    level2 = 1000
    level3 = 1000
    levelCountdown = level1
    onLevel = 'level1'
    score = 0
    scoreWait = 0
    gameRun = True
    
    

def menu():
    button_rect = pygame.Rect(70, 270, 130, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button was clicked
                if button_rect.collidepoint(event.pos):
                    return True
        pygame.display.set_caption("Car Highway Game")
        pygame.display.set_icon(pygame.image.load("CarHighwayLogo.ico"))
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
        scoreXY = (130, 120)
        text1 = font.render(f'Final Score Is', True, (255, 255, 255))
        text2 = font.render(f'{score}', True, (50, 255, 0))
        text2_width = text2.get_width()  # Get the width of the second text surface
        nameUserXY = (130, 240)

        highestScore = int(worksheet.cell('H3').value)
        highestScoreUser = str(worksheet.cell('J3').value)

        if int(worksheet.cell('H3').value) < score:
            highestScore = score
            highestScoreUser = user

            newHighscore = score
            scoreCell = worksheet.cell('H3')
            scoreCell.value = str(newHighscore)
            scoreCell.color = (0.929, 0.490, 0.490) # Red color
            scoreCell.update()
            UserCell = worksheet.cell('J3')
            UserCell.value = str(user)
            UserCell.color = (0.929, 0.694, 0.490) # Orange color
            UserCell.update()



        text3a = font.render(f"Highest Score Ever:", True, (255, 255, 255))
        text3b = font.render(str(highestScore), True, (255, 0, 0))
        text4a = font.render(f"Scored by:", True, (255, 255, 255))
        text4b = font.render(str(highestScoreUser), True, (255, 0, 0))

        text4b_width = text4b.get_width()  # Get the width of the second text surface

        if int(len(str(text2))) > 1:
            scoreXY = (130 - text2_width // 2, 120)  # Center the second text surface in the rectangle
        if int(len(str(text4b))) > 1:
            nameUserXY = (130 - text4b_width // 2, 240)  # Center the second text surface in the rectangle
        screen.blit(text1, (70, 90))
        screen.blit(text2, scoreXY)
        screen.blit(text3a, (40, 150))
        screen.blit(text3b, (119, 180))
        screen.blit(text4a, (85, 210))
        screen.blit(text4b, (nameUserXY))
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
    pygame.display.set_caption("Car Highway Game")
    pygame.display.set_icon(pygame.image.load("CarHighwayLogo.ico"))
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
def crash():
    global gameRun
    pygame.display.set_caption("Car Highway Game")
    pygame.display.set_icon(pygame.image.load("CarHighwayLogo.ico"))
    # gameRun = False 
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
#endregion
    





# while gameTrue == True:
def animate():
    global score, roadSpeed, maxSpeed, minSpeed, level1, level2, level3, levelCountdown, numb, onLevel, roadPos, carPosx, carPosy, carIsRotated, gameRun, obstacle3OnScreen, obstacle2OnScreen, obstacle1OnScreen, laneChosen1, laneChosen3, laneChosen2, images, scoreText, scoreWait, car, carPosx, carPosy, obstacle1posy, obstacle2posy, obstacle3posy, speedObstacle1, speedObstacle2, speedObstacle3, carXspeed, errorWithGame
    global errorTest, gameJustStarted
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    animateLocation = [carPosx - 50, carPosy - 20]
    pygame.display.set_caption("Car Highway Game")
    pygame.display.set_icon(pygame.image.load("CarHighwayLogo.ico"))
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
    
    if speedObstacle1 == speedObstacle2 and speedObstacle2 == speedObstacle3 and gameJustStarted == True:
        errorWithGame = True
        print("A Bug Has Been Fixed!")
        return False
    
    # if errorTest == 0:
    #     print("Successfully Ran Error Test")
    #     errorWithGame = True
    #     errorTest += 1
    #     return False

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
    

    #check for crash
    if carRect.colliderect(obstacle1R):
        return False
    if carRect.colliderect(obstacle2R):
        return False
    if carRect.colliderect(obstacle3R):
        return False
    
    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

    gameJustStarted = False

    #keep going the game
    return True



gameTrue = True

#GAME HERE:
def playGame():
    initVariables()
    isContinue = True
    while isContinue:
        isContinue = animate()
    if errorWithGame == True:
        playGame()
    if errorWithGame != True:
        crash()
        lose()
        return menu()



playAgain = True
while playAgain:
    playAgain = playGame()
    