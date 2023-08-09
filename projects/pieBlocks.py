import pygame

# from collisions import *
pygame.init()

s1, s2 = 100, 50  # block sides
x1, y1 = 1000, 250  # bigger block coords
x2, y2 = 500, y1 + s1 - s2  # smaller block coords

power = int(input('enter: '))  # mass ratio
v1 = (-0.5)  # initial velocity of block 1

m1, m2 = 100 ** (power - 1), 1  # mass of blocks
v2 = 0  # initial velocity of block 2

# temp_x1 = 0
red = (255, 0, 0)
blue = (0, 0, 255)


def message_to_print(msg, color):
    font = pygame.font.SysFont(None, 40)
    text = font.render(msg, True, color)
    win.blit(text, [10, 10])


def reverse_vel(vel):
    '''
    reversing velocity of block
    '''
    vel *= -1
    return vel


def exchange_vel(v1, m1, v2, m2):
    '''
    this function is calculating the new velocity of the block after collision,
    based on law of conservation of momentum and kinetic energy
    '''
    v1 = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2

    return v1  # returning new velocity after collision


win = pygame.display.set_mode((1200, 500))
win.fill((255, 255, 255))
pygame.display.set_caption('simulation')

Collisions = 0  # counting number of collisions
run = True
while run:
    # click_sound = pygame.mixer.Sound("rss/click.wav")
    # pygame.time.delay(10)
    # sound_collide, sound_reverse = True, True

    message_to_print('collision ' + str(Collisions), (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # biger block
    x1 += v1  # changing block coordinates according to velocity
    if x1 >= s2:
        t = x1
        t2 = x2
    else:
        t2 = 0



    if not x2 + s2 < x1 or x1 + s1 < x2:
        '''
        changing velocity after collision,
        storing them in temp variable for each block,
        then assiging new velocity
        '''
        v2_temp = exchange_vel(v2, m2, v1, m1)
        v1_temp = exchange_vel(v1, m1, v2, m2)
        # if sound_collide:
        # click_sound.play()
        # sound = False

        v2, v1 = v2_temp, v1_temp  # assigning new velocities
        Collisions += 1

    # smaller Block
    x2 += v2
    if x2 <= 0:
        '''
        if block 1 touch left wall, its velocity reverses, 
        '''
        v2 = reverse_vel(v2)
        # if sound_reverse:
        # click_sound.play()
        # sound_reverse = False
        Collisions += 1
    pygame.draw.rect(win, blue, (t2, y2, s2, s2)) # x2-> t2
    pygame.draw.rect(win, red, (t, y1, s1, s1))

    pygame.display.update()
    win.fill((255, 255, 255))

pygame.quit()