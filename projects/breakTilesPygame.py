import pygame
import math

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)
orange = (255, 165, 0)
blue = (0, 0, 255)
dGray = (50, 50, 50)

clock = pygame.time.Clock()
FPS = 120
pygame.display.set_caption('Ball shooter')

speed = 5
bx, by = 250, 490
br = 4
ball_exists = False  # Ball existence flag

spacing = 5
rect_width = 10
rect_height = 10

# Create hitboxes and colors for the squares
squares = []
square_colors = [blue] * 330
for y in range(10):
    for x in range(33):
        squares.append(pygame.Rect(x * (rect_width + spacing), y * (rect_height + spacing), rect_width, rect_height))

def shoot():
    global ball_exists, bx, by, shot
    if not ball_exists:
        shot = False
        ball_exists = True

shot = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            if event.button == 1:  # Left mouse button
                shoot()

    screen.fill(dGray)
    ball = pygame.draw.circle(screen, orange, (int(bx), int(by)), br)

    y_position = spacing  # Start position
    for i in range(10):
        x_position = spacing  # Start position
        for j in range(33):
            square_index = i * 33 + j
            pygame.draw.rect(screen, square_colors[square_index], (x_position, y_position, rect_width, rect_height))
            x_position += rect_width + spacing
        y_position += rect_height + spacing

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_y = max(mouse_y, height // 2)
    center_x = width // 2
    center_y = height - rect_height // 2
    pygame.draw.line(screen, red, (center_x, center_y), (mouse_x, mouse_y), 2)

    # Calculate the angle for the arrow
    angle = math.atan2(mouse_y - center_y, mouse_x - center_x)
    arrow_length = 20
    arrow_x = mouse_x - arrow_length * math.cos(angle)
    arrow_y = mouse_y - arrow_length * math.sin(angle)

    # Draw the arrow
    pygame.draw.line(screen, red, (mouse_x, mouse_y), (arrow_x, arrow_y), 2)

    # Move and draw the ball if it exists
    if ball_exists and not shot:
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        shot = True

    if ball_exists:
        bx += vx
        by += vy

        # Check for collisions with squares
        for square in squares:
            square_index = squares.index(square)
            if square.left <= bx + br and square.right >= bx - br and square.top <= by + br and square.bottom >= by - br:
                vy *= -1
                square_colors[square_index] = dGray

    if bx - br <= 0 or bx + br >= width:
        vx *= -1
    if by - br <= 0 or by + br >= height:
        vy *= -1

    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
