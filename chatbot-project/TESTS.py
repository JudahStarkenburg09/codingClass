import pygame
import random
import os

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Car Game')

clock = pygame.time.Clock()

car_image = pygame.image.load('carTop.png')
car_width = 64
car_height = 128

car1_image = pygame.image.load('obstacleCar1.png')
car2_image = pygame.image.load('obstacleCar2.png')


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, (0,0,0))
    game_display.blit(text,(0,0))

def crash():
    print("crash")

def game_loop():
    car_x = (SCREEN_WIDTH - car_width) / 2
    car_y = SCREEN_HEIGHT - car_height
    car_speed = 5

    obstacle_cars = []
    for i in range(5):
        obstacle_cars.append({
            'image': random.choice([car1_image, car2_image]),
            'x': random.randrange(0, SCREEN_WIDTH - car_width),
            'y': random.randrange(-2000, -car_height),
            'speed': random.randrange(4, 10)
        })

    score_count = 0

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        elif keys[pygame.K_RIGHT]:
            car_x += car_speed
        elif keys[pygame.K_UP]:
            car_speed += 0.2
        elif keys[pygame.K_DOWN]:
            car_speed -= 0.2

        game_display.fill(BG_COLOR)

        for obstacle_car in obstacle_cars:
            game_display.blit(obstacle_car['image'], (obstacle_car['x'], obstacle_car['y']))
            obstacle_car['y'] += obstacle_car['speed']

            if obstacle_car['y'] > SCREEN_HEIGHT:
                obstacle_car['y'] = random.randrange(-2000, -car_height)
                obstacle_car['x'] = random.randrange(0, SCREEN_WIDTH - car_width)
                obstacle_car['image'] = random.choice([car1_image, car2_image])
                obstacle_car['speed'] = random.randrange(4, 10)

            if car_y < obstacle_car['y'] + car_height:
                if car_x > obstacle_car['x'] and car_x < obstacle_car['x'] + car_width or car_x + car_width > obstacle_car['x'] and car_x + car_width < obstacle_car['x'] + car_width:
                    crash()
                    pygame.quit()
                    quit()

        game_display.blit(car_image, (car_x, car_y))
        score(score_count)
        score_count += 1

        pygame.display.update()
        clock.tick(60)

game_loop()
