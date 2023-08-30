import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Line settings
line_width = 120
line_height = 10
line_speed = 5
line_x = screen_width // 2 - line_width // 2
line_y = screen_height - line_height

# Ball settings
ball_radius = 20
ball_speed_x = 5
ball_speed_y = 5
ball_x = screen_width // 2
ball_y = screen_height // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        line_x -= line_speed
    if keys[pygame.K_RIGHT]:
        line_x += line_speed
    if keys[pygame.K_UP]:
        line_y -= line_speed
    if keys[pygame.K_DOWN]:
        line_y += line_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0+ball_radius or ball_x >= screen_width-ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0 or ball_y >= screen_height:
        ball_speed_y = -ball_speed_y

    # Ball collision with line
    if (
        line_x <= (ball_x + ball_radius) <= line_x + line_width
        and line_y <= ball_y+ball_radius <= line_y + line_height
    ):
        ball_speed_y = -ball_speed_y

    # Line collision with walls
    if line_x <= 0:
        line_x = 0
    if line_x + line_width >= screen_width:
        line_x = screen_width - line_width
    if line_y <= 0:
        line_y = 0
    if line_y + line_height >= screen_height:
        line_y = screen_height - line_height

    # Clear the screen
    screen.fill(white)

    # Draw the line
    pygame.draw.rect(screen, red, (line_x, line_y, line_width, line_height))

    # Draw the ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
