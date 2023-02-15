

import pygame
pygame.init()

font = pygame.font.Font(None, 36)

#Colores
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

point_player2 = 0
point_player1 = 0

#Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# Coordenadas de la ball
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1

    # Revisa si la ball sale del lado derecho
    if ball_x > 800:
        ball_x = 400
        ball_y = 300
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        point_player1 = point_player1 + 1

    # Revisa si la ball sale del lado izquierdo
    if ball_x < 0:
        ball_x = 400
        ball_y = 300
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        point_player2 = point_player2 + 1

    if point_player1 == 3:
        game_over = True
        print("player 1 wins")
    if point_player2 == 3:
        game_over = True
        print("player 2 wins")


    # Modifica las coordenadas para dar mov. a los jugadores/ ball
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    # Movimiento ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(black)
    #Zona de dibujo
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    # Colisiones
    if ball.colliderect(jugador1) or ball.colliderect(jugador2):
        ball_speed_x *= -1

    pygame.display.flip()
    clock.tick(160)
pygame.quit()