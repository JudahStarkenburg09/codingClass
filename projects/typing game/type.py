import typeData
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for the window size
windowWidth = 800
windowHeight = 600

# Create the window
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Window")

# Define colors
white = (255, 255, 255)

def ifs(key, nextKey, i):
    global colors, tries, alreadyTyped
    if i == nextKey:
        alreadyTyped += i
        if tries == 0:
            add = {
                f"{nextKey}": 'green'
            }
            colors.append(add)
            tries = 0
        if tries == 1:
            add = {
                f"{nextKey}": 'yellow'
            }
            colors.append(add)
            tries = 0
        if tries >= 2:
            add = {
                f"{nextKey}": 'red'
            }
            colors.append(add)
            tries = 0

# Function to handle key presses
def handleKeyPress(key, nextKey):
    global colors, sentence, alreadyTyped, tries

    if key == pygame.K_SPACE:
        i = ' '
        ifs(key, nextKey, i)
    elif key in (pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g,
                 pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                 pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u,
                 pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z):
        i = chr(key)
        ifs(key, nextKey, i)
    else:
        tries += 1

    print(alreadyTyped)

sentence = typeData.sentenceEquals(25)
alreadyTyped = ''
colors = []
tries = 0

# Main game loop
running = True
while running:
    nextKey, numKey = typeData.getNextKey(alreadyTyped)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handleKeyPress(event.key, nextKey)

    # Fill the background with white
    window.fill(white)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Display the sentence in black text
    sentenceText = font.render(sentence, True, (0, 0, 0))
    window.blit(sentenceText, (20, 20))

    # Display typed characters with corresponding colors
    x = 20  # Starting x-coordinate for colored text
    for char, color in zip(alreadyTyped, colors):
        charText = font.render(char, True, pygame.Color(color[char]))
        window.blit(charText, (x, 60))
        x += charText.get_width() + 5  # Adjust the spacing

    # Update the display
    pygame.display.flip()

# Quit pygame and close the window
pygame.quit()
sys.exit()
