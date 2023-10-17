import pygame
import os
import math

currentCwd = os.getcwd()
os.chdir(os.path.join(currentCwd, 'data'))

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True

        # Load car images
        self.carNoWheels = pygame.image.load('carNoWheels.png')
        self.carTurningLeft = pygame.image.load('carTurningLeft.png')
        self.carTurningRight = pygame.image.load('carTurningRight.png')

        # Initial car position and state
        self.carImage = self.carNoWheels
        self.carRect = self.carImage.get_rect()
        self.carRect.center = (400, 300)
        self.carSpeed = 5
        self.carAngle = 0  # Initialize angle to 0

    def updateCarImage(self, leftKey, rightKey):
        if leftKey:
            self.carImage = self.carTurningLeft
        elif rightKey:
            self.carImage = self.carTurningRight
        else:
            self.carImage = self.carNoWheels

    def levelOne(self):
        # Add your logic here
        pass

    def mainLoop(self):
        leftKey = False
        rightKey = False
        forwardKey = False
        backwardKey = False  # Add a key for moving backward

        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftKey = True
                    elif event.key == pygame.K_RIGHT:
                        rightKey = True
                    elif event.key == pygame.K_UP:
                        forwardKey = True
                    elif event.key == pygame.K_DOWN:
                        backwardKey = True  # Set backwardKey to True when the down arrow is pressed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftKey = False
                    elif event.key == pygame.K_RIGHT:
                        rightKey = False
                    elif event.key == pygame.K_UP:
                        forwardKey = False
                    elif event.key == pygame.K_DOWN:
                        backwardKey = False  # Set backwardKey to False when the down arrow is released

            # Update car image based on arrow keys
            self.updateCarImage(leftKey, rightKey)

            # Move the car forward and backward
            if forwardKey:
                self.carRect.x += self.carSpeed * math.cos(self.carAngle)
                self.carRect.y -= self.carSpeed * math.sin(self.carAngle)
            if backwardKey:  # Move backward when the backward key is pressed
                self.carRect.x -= self.carSpeed * math.cos(self.carAngle)
                self.carRect.y += self.carSpeed * math.sin(self.carAngle)

            self.screen.fill((40, 40, 40))  # Fill the screen with a background color
            self.screen.blit(self.carImage, self.carRect)
            pygame.display.flip()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.mainLoop()
