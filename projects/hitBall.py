import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen settings
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ball Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Line settings
paddleWidth = 120
paddleHeight = 10
paddleSpeed = 7
paddleX = screenWidth // 2 - paddleWidth // 2
paddleY = screenHeight - paddleHeight
paddleRotation = 0  # Initial rotation angle

# Ball settings
ballRadius = 20
ballSpeedX = paddleSpeed - 2
ballSpeedY = paddleSpeed - 2
ballX = screenWidth // 2
ballY = screenHeight // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddleX -= paddleSpeed
    if keys[pygame.K_RIGHT]:
        paddleX += paddleSpeed
    if keys[pygame.K_UP]:
        paddleY -= paddleSpeed
    if keys[pygame.K_DOWN]:
        paddleY += paddleSpeed

    # Rotation controls
    if keys[pygame.K_RCTRL]:
        paddleRotation += 2  # Rotate counter-clockwise
    if keys[pygame.K_KP0]:
        paddleRotation -= 2  # Rotate clockwise

    # Update ball position
    ballX += ballSpeedX
    ballY += ballSpeedY

    # Ball collision with walls
    if ballX <= ballRadius or ballX >= screenWidth - ballRadius:
        ballSpeedX = -ballSpeedX
    if ballY <= ballRadius or ballY >= screenHeight - ballRadius:
        ballSpeedY = -ballSpeedY

    # Line collision with walls
    if paddleX <= 0:
        paddleX = 0
    if paddleX + paddleWidth >= screenWidth:
        paddleX = screenWidth - paddleWidth
    if paddleY <= 0:
        paddleY = 0
    if paddleY + paddleHeight >= screenHeight:
        paddleY = screenHeight - paddleHeight

    # Clear the screen
    screen.fill(white)

    # Draw the rotating paddle
    rotated_paddle = pygame.transform.rotate(pygame.Surface((paddleWidth, paddleHeight)), paddleRotation)
    paddle_rect = rotated_paddle.get_rect(center=(paddleX + paddleWidth // 2, paddleY + paddleHeight // 2))
    screen.blit(rotated_paddle, paddle_rect.topleft)

    # Draw the ball
    ball = pygame.draw.circle(screen, red, (ballX, ballY), ballRadius)

    # Create a Rect object for the ball
    ball_rect = pygame.Rect(ballX - ballRadius, ballY - ballRadius, ballRadius * 2, ballRadius * 2)

    if ball_rect.colliderect(paddle_rect):
        ballSpeedY = -ballSpeedY

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
