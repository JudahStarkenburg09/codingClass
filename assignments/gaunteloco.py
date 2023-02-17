import pygame
import time
import random
import os

current_directory = os.getcwd()
folder1 = 'assignments'
os.chdir(os.path.join(current_directory, folder1))
runningMenu = True

def mouseGame():
    pygame.init()
    losses = 0
    caught = 0
    speedInc = 0.2
    speed1 = random.uniform(5, 10) #INITIAL SPEED FOR BALL1
    posNeg1 = random.randint(1,2)
    randx1 = random.randint(100,900)

    speed2 = random.uniform(5, 10) #INITIAL SPEED FOR BALL2
    posNeg2 = random.randint(1,2)
    randx2 = random.randint(100,900)



    width, height = 1000, 650
    screen = pygame.display.set_mode((width, height))

    ball1 = pygame.image.load("baseball.png")
    x1 = randx1
    y1 = 0
    ball2 = pygame.image.load("baseball.png")
    x2 = 666
    y2 = 50
    glove = pygame.image.load("glove.png")
    x3 = 300
    y3 = 300
    background = pygame.image.load("field.png")

    screen.blit(background, (0, 0))
    screen.blit(ball1,(x1, y1))
    screen.blit(ball2,(x2, y2))
    screen.blit(glove,(x3, y3))

    glove_rect = glove.get_rect(x=x3, y=y3)
    ball1_rect = ball1.get_rect(x=x1, y=y1)
    ball2_rect = ball2.get_rect(x=x2, y=y2)




    running = True
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Update the glove position to follow the mouse
        x3 = mouse_x - glove_rect.width / 2
        y3 = mouse_y - glove_rect.height / 2




        if posNeg1 == 1:
            x1 = x1 + speed1
            y1 = y1 + speed1
        if posNeg1 == 2:
            x1 = x1 - speed1
            y1 = y1 + speed1

        if posNeg2 == 1:
            x2 = x2 + speed2
            y2 = y2 + speed2
        if posNeg2 == 2:
            x2 = x2 - speed2
            y2 = y2 + speed2

        screen.blit(background, (0, 0))
        screen.blit(ball1,(x1, y1))
        screen.blit(ball2,(x2, y2))
        screen.blit(glove,(x3, y3))


        glove_rect = glove.get_rect(x=x3, y=y3)
        ball1_rect = ball1.get_rect(x=x1, y=y1)
        ball2_rect = ball2.get_rect(x=x2, y=y2)

        #All Collisions
        if x1 < 0: #Bounce ball1 off left side
            posNeg1 = 1
        if x1 > 950: #Bounce ball1 off right side
            posNeg1 = 2
        if x2 < 0: #Bounce ball2 off left side
            posNeg2 = 1
        if x2 > 950: #Bounce ball2 off right side
            posNeg2 = 2
        if ball1_rect.colliderect(glove_rect): #Collision ball1 with glove, resets up to top
            speedInc += 0.8
            speed1 = (random.uniform(5, 12) + speedInc)
            posNeg1 = random.randint(1, 2)
            randx1 = random.randint(100, 900)
            caught += 1
            x1 = randx1
            y1 = 000
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play()
        if ball2_rect.colliderect(glove_rect): #Collision ball2 with glove, resets up to top
            speedInc += 0.8
            speed2 = (random.uniform(5, 12) + speedInc)
            posNeg2 = random.randint(1, 2)
            randx2 = random.randint(100, 900)
            caught += 1
            x2 = randx2
            y2 = 000
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play()
        if y1 > 650: #Ball1 makes it to bottom
            speed1 = random.uniform(5, 12)
            posNeg1 = random.randint(1, 2)
            randx1 = random.randint(100, 900)
            losses += 1
            x1 = randx1
            y1 = 000
            pygame.mixer.music.load('lose.mp3')
            pygame.mixer.music.play()
        if y2 > 650: #Ball2 makes it to bottom
            speed2 = random.uniform(5, 12)
            posNeg2 = random.randint(1, 2)
            randx2 = random.randint(100, 900)
            losses += 1
            x2 = randx2
            y2 = 000
            pygame.mixer.music.load('lose.mp3')
            pygame.mixer.music.play()
        if x3 < -5: #Bounce glove off left side
            x3 = x3 + 16
        if y3 > 570: #Bounce glove off bottom
            y3 = y3 - 16
        if x3 > 910: #Bounce glove off right side
            x3 = x3 - 16
        if y3 < 0:  #Bounce glove off top
            y3 = y3 + 16
        liveLeft = 10 - losses
        font = pygame.font.Font(None, 30)
        score = font.render("Score: " + str(caught) + " :-: " + str(liveLeft), True, (0, 0, 0))
        screen.blit(score, (860,10))
        if liveLeft <= 0:
            pygame.mixer.music.stop()
            os.system("cls")
            print("\n")
            print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
            print("GAME OVER! FINAL SCORE: " + str(caught))
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("\n")
            pygame.quit()
            break
        time.sleep(.03) #ALL ANIMATIONS SPEED
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()






def arrowKeyGame():
    pygame.init()
    losses = 0
    caught = 0
    speedInc = 0.2
    speed1 = random.uniform(5, 10) #INITIAL SPEED FOR BALL1
    posNeg1 = random.randint(1,2)
    randx1 = random.randint(100,900)

    speed2 = random.uniform(5, 10) #INITIAL SPEED FOR BALL2
    posNeg2 = random.randint(1,2)
    randx2 = random.randint(100,900)



    width, height = 1000, 650
    screen = pygame.display.set_mode((width, height))

    ball1 = pygame.image.load("baseball.png")
    x1 = randx1
    y1 = 0
    ball2 = pygame.image.load("baseball.png")
    x2 = 666
    y2 = 50
    glove = pygame.image.load("glove.png")
    x3 = 300
    y3 = 300
    background = pygame.image.load("field.png")

    screen.blit(background, (0, 0))
    screen.blit(ball1,(x1, y1))
    screen.blit(ball2,(x2, y2))
    screen.blit(glove,(x3, y3))

    glove_rect = glove.get_rect(x=x3, y=y3)
    ball1_rect = ball1.get_rect(x=x1, y=y1)
    ball2_rect = ball2.get_rect(x=x2, y=y2)




    running = True
    while running:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x3 -= 16
        if keys[pygame.K_RIGHT]:
            x3 += 16
        if keys[pygame.K_UP]:
            y3 -= 16
        if keys[pygame.K_DOWN]:
            y3 += 16




        if posNeg1 == 1:
            x1 = x1 + speed1
            y1 = y1 + speed1
        if posNeg1 == 2:
            x1 = x1 - speed1
            y1 = y1 + speed1

        if posNeg2 == 1:
            x2 = x2 + speed2
            y2 = y2 + speed2
        if posNeg2 == 2:
            x2 = x2 - speed2
            y2 = y2 + speed2

        screen.blit(background, (0, 0))
        screen.blit(ball1,(x1, y1))
        screen.blit(ball2,(x2, y2))
        screen.blit(glove,(x3, y3))


        glove_rect = glove.get_rect(x=x3, y=y3)
        ball1_rect = ball1.get_rect(x=x1, y=y1)
        ball2_rect = ball2.get_rect(x=x2, y=y2)

        #All Collisions
        if x1 < 0: #Bounce ball1 off left side
            posNeg1 = 1
        if x1 > 950: #Bounce ball1 off right side
            posNeg1 = 2
        if x2 < 0: #Bounce ball2 off left side
            posNeg2 = 1
        if x2 > 950: #Bounce ball2 off right side
            posNeg2 = 2
        if ball1_rect.colliderect(glove_rect): #Collision ball1 with glove, resets up to top
            speedInc += 0.8
            speed1 = (random.uniform(5, 12) + speedInc)
            posNeg1 = random.randint(1, 2)
            randx1 = random.randint(100, 900)
            caught += 1
            x1 = randx1
            y1 = 000
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play()
        if ball2_rect.colliderect(glove_rect): #Collision ball2 with glove, resets up to top
            speedInc += 0.8
            speed2 = (random.uniform(5, 12) + speedInc)
            posNeg2 = random.randint(1, 2)
            randx2 = random.randint(100, 900)
            caught += 1
            x2 = randx2
            y2 = 000
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play()
        if y1 > 650: #Ball1 makes it to bottom
            speed1 = random.uniform(5, 12)
            posNeg1 = random.randint(1, 2)
            randx1 = random.randint(100, 900)
            losses += 1
            x1 = randx1
            y1 = 000
            pygame.mixer.music.load('lose.mp3')
            pygame.mixer.music.play()
        if y2 > 650: #Ball2 makes it to bottom
            speed2 = random.uniform(5, 12)
            posNeg2 = random.randint(1, 2)
            randx2 = random.randint(100, 900)
            losses += 1
            x2 = randx2
            y2 = 000
            pygame.mixer.music.load('lose.mp3')
            pygame.mixer.music.play()
        if x3 < -5: #Bounce glove off left side
            x3 = x3 + 16
        if y3 > 570: #Bounce glove off bottom
            y3 = y3 - 16
        if x3 > 910: #Bounce glove off right side
            x3 = x3 - 16
        if y3 < 0:  #Bounce glove off top
            y3 = y3 + 16
        liveLeft = 10 - losses
        font = pygame.font.Font(None, 30)
        score = font.render("Score: " + str(caught) + " :-: " + str(liveLeft), True, (0, 0, 0))
        screen.blit(score, (860,10))
        if liveLeft <= 0:
            pygame.mixer.music.stop()
            os.system("cls")
            print("\n")
            print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
            print("GAME OVER! FINAL SCORE: " + str(caught))
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("\n")
            pygame.quit()
            break

        time.sleep(.03) #ALL ANIMATIONS SPEED
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()







while runningMenu:
    pygame.init()
    # Handle events
    # Set up the menu screen
    width1, height1 = 1000, 650
    menu = pygame.display.set_mode((width1, height1))

    # Set up the font for the button labels
    font = pygame.font.Font(None, 50)

    # Set up the first button
    button1 = pygame.Rect(300, 200, 400, 100)  # x, y, width, height
    label1 = font.render("Play With Arrow Keys", True, (255, 255, 255))  # text, antialiasing, color

    # Set up the second button
    button2 = pygame.Rect(300, 350, 400, 100)
    label2 = font.render("Play With Mouse", True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningMenu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is clicked on a button
            if button1.collidepoint(event.pos):
                arrowKeyGame()
            elif button2.collidepoint(event.pos):
                mouseGame()

    # Check if the mouse is currently hovering over a button, and change its color accordingly
    if button1.collidepoint(pygame.mouse.get_pos()):
        button1_color = (100, 100, 255)  # blue+
    else:
        button1_color = (0, 0, 255)  # blue

    if button2.collidepoint(pygame.mouse.get_pos()):
        button2_color = (100, 100, 255)  # blue+
    else:
        button2_color = (0, 0, 255)  # blue

    # Draw the buttons and labels
    pygame.draw.rect(menu, button1_color, button1)
    pygame.draw.rect(menu, button2_color, button2)
    menu.blit(label1, (button1.centerx - label1.get_width() // 2, button1.centery - label1.get_height() // 2))
    menu.blit(label2, (button2.centerx - label2.get_width() // 2, button2.centery - label2.get_height() // 2))

    # Update the display
    pygame.display.update()



    