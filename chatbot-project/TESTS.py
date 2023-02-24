import pygame
import random

# initialize pygame
pygame.init()

# create window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Dodge Game")

# set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# set up game variables
player_size = 50
player_pos = [screen_width // 2, screen_height - player_size * 2]
player_speed = 10

car_size = 50
car_speed = 5
car_list = []
for i in range(5):
    car_pos = [random.randint(0, screen_width - car_size), -car_size]
    car_list.append(car_pos)

# set up game loop
game_over = False
clock = pygame.time.Clock()

# define functions
def draw_player():
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))

def move_player(key):
    if key == pygame.K_LEFT:
        player_pos[0] -= player_speed
    elif key == pygame.K_RIGHT:
        player_pos[0] += player_speed

def draw_car(car_pos):
    pygame.draw.rect(screen, red, (car_pos[0], car_pos[1], car_size, car_size))

def move_cars():
    global car_list
    for i, car_pos in enumerate(car_list):
        if car_pos[1] > screen_height:
            car_list.pop(i)
            new_car_pos = [random.randint(0, screen_width - car_size), -car_size]
            car_list.append(new_car_pos)
        else:
            car_pos[1] += car_speed

def check_collision():
    global game_over
    for car_pos in car_list:
        if detect_collision(player_pos, car_pos):
            game_over = True

def detect_collision(player_pos, car_pos):
    player_x = player_pos[0]
    player_y = player_pos[1]
    car_x = car_pos[0]
    car_y = car_pos[1]

    if (car_x >= player_x and car_x < (player_x + player_size)) or (player_x >= car_x and player_x < (car_x + car_size)):
        if (car_y >= player_y and car_y < (player_y + player_size)) or (player_y >= car_y and player_y < (car_y + car_size)):
            return True
    return False

# game loop
while not game_over:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move_player(event.key)

    # move cars
    move_cars()

    # check for collision
    check_collision()

    # draw objects
    screen.fill(black)
    draw_player()
    for car_pos in car_list:
        draw_car(car_pos)

    # update display
    pygame.display.update()

    # set frame rate
    clock.tick(60)

# quit game
pygame.quit()
