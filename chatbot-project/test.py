import pygame

# initialize Pygame
pygame.init()

# set the screen size
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set the font and font size
font = pygame.font.Font(None, 30)

# define the notification message and colors
notification_text = "Error detected, and fixed!"
notification_color = (255, 0, 0)
background_color = (255, 255, 255)

# set the notification position and animation parameters
notification_x = screen_width
notification_y = 50
notification_speed = 5
notification_visible = False

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the screen background
    screen.fill(background_color)

    # update the notification position and visibility
    if notification_visible:
        notification_x -= notification_speed
        if notification_x < -font.size(notification_text)[0]:
            notification_visible = False
    else:
        notification_x = screen_width
        notification_visible = True

    # draw the notification text
    if notification_visible:
        notification_surface = font.render(notification_text, True, notification_color)
        screen.blit(notification_surface, (notification_x, notification_y))

    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()
