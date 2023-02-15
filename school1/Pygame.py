import pygame
import time
import os

current_directory = os.getcwd()
folder1 = 'school1'
os.chdir(os.path.join(current_directory, folder1))

pygame.init()

width, height = 640, 350
screen = pygame.display.set_mode((width, height))

# Load background image
background = pygame.image.load("background.png")

# Create two paddles
paddle_width = 20
paddle_height = 100
paddle1_x = 20
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 20
paddle2_y = height // 2 - paddle_height // 2

# Create ball
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Initialize scores
player1_score = 0
player2_score = 0

# Set up font for scoreboard
font = pygame.font.Font(None, 30)

# while countdown < 4

# Set up countdown timer
countdown_time = 3
start_ticks = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        
    # Check for player 1 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    
    # Check for player 2 movement
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5
    
    # Keep paddles within screen bounds
    if paddle1_y < 0:
        paddle1_y = 0
    if paddle1_y > height - paddle_height:
        paddle1_y = height - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > height - paddle_height:
        paddle2_y = height - paddle_height
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Check for ball collisions with walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y
    if ball_x - ball_radius <= paddle_width and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle_height:
        ball_speed_x = -ball_speed_x
    if ball_x + ball_radius >= width - paddle_width and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -ball_speed_x
    
    # Check for ball going out of bounds (player scores)
    if ball_x < 0:
        player2_score += 1
        ball_x = width // 2
        ball_y = height // 2
    if ball_x > width:
        player1_score += 1
        ball_x = width // 2
        ball_y = height // 2
    
    # Check for win condition
    if player1_score == 3 or player2_score == 3:
        running = False
    
    # Clear screen and draw background
    screen.blit(background, (0, 0))
    
    # Draw paddles
    pygame.draw.rect(screen, (255, 255, 255), (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle2_x, paddle2_y, paddle_width, paddle_height))
    
    # Draw ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    
    # Draw scoreboard
    player1_text = font.render("Player 1: " + str(player1_score), True, (255, 255, 255))
    player2_text = font.render("Player 2: " + str(player2_score), True, (255, 255, 255))
    screen.blit(player1_text, (width // 4, 10))
    screen.blit(player2_text, (width // 4 * 3, 10))
    
    # Check for win condition
    if player1_score == 5 or player2_score == 5:
        win_text = font.render("Player " + str(1 if player1_score == 3 else 2) + " wins!", True, (255, 255, 255))
        screen.blit(win_text, (width // 2 - 70, height // 6))
        pygame.display.update()
        time.sleep(3)
        running = False
        break

    time.sleep(.01)
    
    # Show the screen
    pygame.display.update()

# Quit pygame
pygame.quit()

    
