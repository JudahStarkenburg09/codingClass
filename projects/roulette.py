import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants for the window dimensions
WIDTH, HEIGHT = 400, 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR_ADD = (0, 128, 255)
BUTTON_COLOR_START = (0, 128, 0)

# Create a Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("List Manager")

# Font for text
font = pygame.font.Font(None, 36)

# List to store items
item_list = []

# Input field
input_rect = pygame.Rect(50, 50, 300, 50)
input_color = pygame.Color('lightskyblue3')
input_text = ''
input_active = False
cursor_timer = 0
backspace_timer = 0
initial_backspace_delay = 120  # Initial delay in frames (1 second)
backspace_interval = 6  # Interval for subsequent character removal (0.25 second)

# Set the frame rate (frames per second)
fps = 60
clock = pygame.time.Clock()

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (x, y))

def draw_cursor(x, y, text):
    cursor_x = x + font.size(text[:cursor_timer])[0]
    pygame.draw.line(window, BLACK, (cursor_x, y), (cursor_x, y + font.get_height()))

def main():
    global input_text, item_list, input_active, cursor_timer, backspace_timer
    running = True
    add_button = pygame.Rect(50, 120, 100, 50)
    start_button = pygame.Rect(50, 200, 100, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if add_button.collidepoint(event.pos):
                    if input_text:
                        item_list.append(input_text)
                        input_text = ''
                if start_button.collidepoint(event.pos):
                    print("List contents:")
                    for item in item_list:
                        print(item)
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        backspace_timer = 0
                        if len(input_text) > 0:
                            input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text:
                            item_list.append(input_text)
                            input_text = ''
                    else:
                        if len(input_text) < 20:
                            input_text += event.unicode
                            cursor_timer = len(input_text)

            if event.type == pygame.KEYUP:
                if input_active and event.key == pygame.K_BACKSPACE:
                    backspace_timer = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                    cursor_timer = len(input_text)

        window.fill(WHITE)

        # Draw buttons
        pygame.draw.rect(window, BUTTON_COLOR_ADD, add_button)
        pygame.draw.rect(window, BUTTON_COLOR_START, start_button)

        # Draw text and cursor
        draw_text("Add", 75, 135)
        draw_text("Start", 70, 215)

        # Draw input box
        pygame.draw.rect(window, input_color, input_rect, 2)

        if input_active:
            draw_text(input_text, input_rect.x + 5, input_rect.y + 5)
            draw_cursor(input_rect.x + 5, input_rect.y + 5, input_text)

            # Hold backspace to remove multiple characters
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                if backspace_timer == 0:
                    # Initial delay before starting character removal
                    if time.time() - backspace_start_time >= 1:  # 1 second delay
                        backspace_timer = initial_backspace_delay
                elif backspace_timer > 0:
                    backspace_timer -= 1
                    if backspace_timer % backspace_interval == 0:
                        if len(input_text) > 0:
                            input_text = input_text[:-1]
            else:
                backspace_timer = 0  # Reset the backspace timer if the key is released

        pygame.display.flip()

        # Limit the frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()

while True:
    backspace_start_time = time.time()
    main()
    break
