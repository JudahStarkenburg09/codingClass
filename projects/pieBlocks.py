import pygame
import sys
import tkinter as tk

def save_answer():
    global answer
    answer = entry.get()
    weight.destroy()

def on_enter(event):
    save_answer()

def on_closing():
    # Any cleanup or saving actions can be placed here
    exit()

weight = tk.Tk()
weight.geometry('300x200')
weight.title('Weight')
weight.protocol("WM_DELETE_WINDOW", on_closing)

question = tk.Label(weight, text="Enter the amount of weight for the block (kg)")
question.place(x=5, y=20)

entry = tk.Entry(weight)
entry.pack(padx=20, pady=50)
entry.bind("<Return>", on_enter)


weight.mainloop()






# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Simulation")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Create blocks
block1_mass = 1
block2_mass_red = int(answer)
speed = 1


block1_width = 40
block1_height = 40
block1_x = 50
block1_y = screen_height - block1_height
block1_vx = 0

block2_width = 40
block2_height = 40
block2_x = 300
block2_y = screen_height - block2_height
block2_vx = -speed
collision_count = 0

# Create wall
wall_color = (0, 0, 0)
wall_thickness = 5
black = (0,0,0)
# Create font
font1 = pygame.font.Font(None, 20)
font2 = pygame.font.Font(None, 30)


def draw_wall():
    pygame.draw.line(screen, wall_color, (0, 0), (0, screen_height), wall_thickness)

def draw_weights():
    text_block1 = font1.render(f"{block1_mass} kg", True, black)
    text_block2 = font1.render(f"{block2_mass_red} kg", True, black )
    screen.blit(text_block1, (block1_x +5, block1_y-20))
    screen.blit(text_block2, (block2_x +5, block2_y-20))

def update_velocity(m1, v1, m2, v2):
    new_v1 = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
    new_v2 = (2 * m1 / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
    return new_v1, new_v2

# Main loop
def main():
    global block1_x, block2_x, block1_vx, block2_vx, block1_mass, block2_mass_red, collision_count
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        draw_wall()

        # Update block positions
        block1_x += block1_vx
        block2_x += block2_vx

        # Check collisions
    
        if block1_x + block1_width >= block2_x:
            block1_vx, block2_vx = update_velocity(block1_mass, block1_vx, block2_mass_red, block2_vx)
            collision_count += 1

        if block1_x <= 0:
            block1_vx *= -1
            collision_count +=1

        if block2_x <= 0:
            block2_vx *= -1

        # Draw blocks
        pygame.draw.rect(screen, blue, (block1_x, block1_y, block1_width, block1_height))
        pygame.draw.rect(screen, red, (block2_x, block2_y, block2_width, block2_height))

        text_collision_count = font2.render(f"Collisions: {collision_count}", True, (0, 0, 0))
        screen.blit(text_collision_count, (20, 100))
        draw_weights()

        pygame.display.update()
        clock.tick(60)



main()