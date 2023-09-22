import pygame
import sys
import tkinter as tk
import random
import os
import time

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chopsticks")

# Colors
WHITE = (255, 255, 255)

fingerAmountLeft = 1
fingerAmountRight = 1

turn = 1 # 1 = player, 2= bot

selectedHand = None

botFingerAmountLeft = 1
botFingerAmountRight = 1

def botTurn():
    global botFingerAmountRight, botFingerAmountLeft, fingerAmountLeft, fingerAmountRight, turn, selected4, selected3, selected2, selected1

    print("Bot's turn")

    attack = None
    for i in range(1,3):
        if i == 1:
            if botFingerAmountLeft + fingerAmountLeft == 5:
                attack = ('left', 'left')
            elif botFingerAmountLeft + fingerAmountRight == 5:
                attack = ('left', 'right')
        if i == 2:
            if botFingerAmountRight + fingerAmountLeft == 5:
                attack = ('right', 'left')
            elif botFingerAmountRight + fingerAmountLeft == 5:
                attack = ('right', 'right')
    if attack == None:
        rAttack = random.randint(1,6)
        if rAttack == 1:
            attack = ('left', 'left')
        elif rAttack == 2:
            attack = ('left', 'right')
        elif rAttack == 3:
            attack = ('right', 'left')
        elif rAttack == 4:
            attack = ('right', 'right')
        elif rAttack == 5:
            desiredSum = botFingerAmountLeft + botFingerAmountRight
            maxAttempts = 500
            attempts = 0
            while True:
                print('thinking...')
                attempts += 1
                if attempts >= maxAttempts:
                    rAttack = random.randint(1,5)
                    if rAttack == 1:
                        attack = ('left', 'left')
                    elif rAttack == 2:
                        attack = ('left', 'right')
                    elif rAttack == 3:
                        attack = ('right', 'left')
                    elif rAttack == 4:
                        attack = ('right', 'right')
                    print(attack)
                    break
                n1 = random.randint(1,5)
                n2 = random.randint(1,5)
                if (n1+n2) == desiredSum and (botFingerAmountLeft != n1) and (botFingerAmountRight != n1):
                    break

            if (n1 + fingerAmountLeft) >= 5 or (n1 + fingerAmountRight) >= 5 or (n2 + fingerAmountRight) >= 5 or (n2 + fingerAmountLeft) >= 5:
                rAttack = random.randint(1,5)
                if rAttack == 1:
                    attack = ('left', 'left')
                elif rAttack == 2:
                    attack = ('left', 'right')
                elif rAttack == 3:
                    attack = ('right', 'left')
                elif rAttack == 4:
                    attack = ('right', 'right')

    if attack:
        os.system('cls')
        print(attack)
        hand, attacking = attack
        if hand == 'left':
            if attacking == 'left':
                if fingerAmountLeft == 0 or botFingerAmountLeft == 0:
                    botTurn()
                fingerAmountLeft += botFingerAmountLeft
                selected1 = 'green'
            if attacking == 'right':
                if fingerAmountRight == 0 or botFingerAmountRight == 0:
                    botTurn()
                fingerAmountRight += botFingerAmountLeft
                selected2 = 'green'
            selected4 = 'green'
        elif hand == 'right':
            if attacking == 'left':
                if fingerAmountLeft == 0 or botFingerAmountLeft == 0:
                    botTurn()
                fingerAmountLeft += botFingerAmountRight
                selected1 = 'green'
            if attacking == 'right':
                if fingerAmountRight == 0 or botFingerAmountRight == 0:
                    botTurn()
                fingerAmountRight += botFingerAmountRight
                selected2 = 'green'
            selected3 = 'green'

    turn = 1  # Set the turn back to the player



def handleSplit(fingerAmounts, totalHand):
    global fingerAmountLeft, fingerAmountRight
    mini = tk.Tk()
    mini.geometry('200x100')
    mini.title("Split")

    left_entry = tk.Entry(mini, width=5)
    left_entry.pack(side=tk.LEFT)

    right_entry = tk.Entry(mini, width=5)
    right_entry.pack(side=tk.RIGHT)

    def checkNumbers():
        global fingerAmountRight, fingerAmountLeft
        left = left_entry.get()
        right = right_entry.get()

        if left.isdigit() and right.isdigit() and int(left) + int(right) == totalHand and int(left) != fingerAmounts[2] and int(left) != fingerAmounts[3] and int(left) != 5 and int(right) != 5:
            fingerAmounts[2] = left
            fingerAmounts[3] = right
            mini.destroy()
            fingerAmountLeft = int(fingerAmounts[2])
            fingerAmountRight = int(fingerAmounts[3])
            return
        else:
            invalid = tk.Label(mini, text="Invalid Split!")
            invalid.place(x=66, y=50)


    mini.bind("<Return>", lambda event: checkNumbers())

    button = tk.Button(mini, text="Check", command=checkNumbers)
    button.pack()

    mini.mainloop()


winner = None

def drawPlayerFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 525, 20, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 525), 10)

def drawBotFinger(xr, xa):
    pygame.draw.rect(screen, (0, 0, 0),  (xr, 0, 20, 75))
    pygame.draw.circle(screen, (0, 0, 0), (xa, 75), 10)

def split():
    global botFingerAmountRight, botFingerAmountLeft, fingerAmountLeft, fingerAmountRight, turn
    totalHand = fingerAmountRight + fingerAmountLeft
    fingerAmounts = [botFingerAmountRight, botFingerAmountLeft, fingerAmountLeft, fingerAmountRight]
    handleSplit(fingerAmounts, totalHand)
    turn = 2
    return

def add(selectedHand, bn):
    global botFingerAmountRight, botFingerAmountLeft, fingerAmountLeft, fingerAmountRight, turn
    if selectedHand:
        print(f"Selected hand is {selectedHand} and adding to hand {bn}")
        if selectedHand == 3:
            if bn == 1 and botFingerAmountLeft > 0:
                botFingerAmountLeft += fingerAmountLeft
            elif bn == 2 and botFingerAmountRight > 0:
                botFingerAmountRight += fingerAmountLeft
        elif selectedHand == 4:
            if bn == 1 and botFingerAmountLeft > 0:
                botFingerAmountLeft += fingerAmountRight
            elif bn == 2 and botFingerAmountRight > 0:
                botFingerAmountRight += fingerAmountRight
        else:
            return selectedHand, bn
        
        selectedHand = None
        turn = 2
        return selectedHand, bn


# Define a function for button actions
def button_action(bn):
    global selectedHand
    if bn == 'split':
        split()
    elif (bn == 1 or bn == 2) and (selectedHand == 3 or selectedHand == 4):
        selectedHand, bn = add(selectedHand, bn)
    elif (selectedHand == 3 or selectedHand == 4) and (bn == 3 or bn == 4):
        selectedHand = None
    else:
        selectedHand = bn

selected1 = 'yellow'
selected2 = 'yellow'
selected3 = 'yellow'
selected4 = 'yellow'
# Main game loop

def win():
    global winner
    if winner == 1:
        print("Player wins!")
    elif winner == 2:
        print("Bot Wins!")

waitTick = 0

flashTick = 0

mouse_button_down = False
button_clicked = None
running = True
while running:  # Your main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button down
            for i in range(1, 6):
                if i == 5:
                    button_rect = splitb
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        button_clicked = 'split'
                else:
                    button_rect = globals()[f"b{i}"]
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        button_clicked = i

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button up
            if button_clicked is not None:
                button_action(button_clicked)
                button_clicked = None

    if botFingerAmountLeft == 0 and botFingerAmountRight == 0:
        winner = 1
        turn = None
        running = False
        win()

    if fingerAmountLeft == 0 and fingerAmountRight == 0:
        winner = 2
        turn = None
        running = False
        win()



    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Clear the screen
    screen.fill(WHITE)

    for i in range(0, fingerAmountLeft):
        xr = 50 + (i*40)
        xa = 60 + (i*40)
        drawPlayerFinger(xr, xa)

    for i in range(0, fingerAmountRight):
        xr = 725 - (i*40)
        xa = 735 - (i*40)
        drawPlayerFinger(xr, xa)

    for i in range(0, botFingerAmountLeft):
        xr = 50 + (i*40)
        xa = 60 + (i*40)
        drawBotFinger(xr, xa)

    for i in range(0, botFingerAmountRight):
        xr = 725 - (i*40)
        xa = 735 - (i*40)
        drawBotFinger(xr, xa)

    if flashTick >= 1000:
        flashTick = 0
        selected3 = 'yellow'
        selected4 = 'yellow'
        selected1 = 'yellow'
        selected2 = 'yellow'
    elif selected3 == 'green' or selected4 == 'green':
        flashTick += 1

    # Draw buttons and check for clicks
    if botFingerAmountLeft > 0:
        b1 = pygame.draw.rect(screen, selected4, (110, 100, 50, 50))
    if botFingerAmountRight > 0:
        b2 = pygame.draw.rect(screen, selected3, (650, 100, 50, 50))
    if fingerAmountLeft > 0:
        b3 = pygame.draw.rect(screen, selected1, (110, 450, 50, 50))
    if fingerAmountRight > 0:
        b4 = pygame.draw.rect(screen, selected2, (650, 450, 50, 50))

    splitb = pygame.draw.rect(screen, 'yellow', (375, 500, 50, 50))


    
    if selectedHand == 3:
        selected1 = "green"
        selected2 = "yellow"
    elif selectedHand == 4:
        selected1 = "yellow"
        selected2 = "green"
    elif selected4 != 'green' and selected3 != 'green':
        selected1 = "yellow"
        selected2 = "yellow"

    if fingerAmountLeft >= 5:
        fingerAmountLeft = 0
    if fingerAmountRight >= 5:
        fingerAmountRight = 0
    if botFingerAmountLeft >= 5:
        botFingerAmountLeft = 0
    if botFingerAmountRight >= 5:
        botFingerAmountRight = 0

    if turn == 2:
        if waitTick >= 1000:
            botTurn()
            waitTick == 0
        else:
            waitTick += 1

    time.sleep(0.001)
    pygame.display.flip()

pygame.quit()
sys.exit()

