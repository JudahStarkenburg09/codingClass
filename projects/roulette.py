import pygame
import sys
import time

class ListManager:
    def __init__(self):
        pygame.init()

        # Constants for the window dimensions
        self.WIDTH, self.HEIGHT = 400, 400

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BUTTON_COLOR_ADD = (0, 128, 255)
        self.BUTTON_COLOR_START = (0, 128, 0)

        # Create a Pygame window
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("List Manager")

        # Font for text
        self.font = pygame.font.Font(None, 36)

        # List to store items
        self.item_list = []

        # Input field
        self.input_rect = pygame.Rect(50, 50, 300, 50)
        self.input_color = pygame.Color('lightskyblue3')
        self.input_text = ''
        self.input_active = False
        self.cursor_timer = 0
        self.backspace_timer = 0
        self.initial_backspace_delay = 120  # Initial delay in frames (1 second)
        self.backspace_interval = 6  # Interval for subsequent character removal (0.25 second)

        # Set the frame rate (frames per second)
        self.fps = 60
        self.clock = pygame.time.Clock()

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.BLACK)
        self.window.blit(text_surface, (x, y))

    def draw_cursor(self, x, y, text):
        cursor_x = x + self.font.size(text[:self.cursor_timer])[0]
        pygame.draw.line(self.window, self.BLACK, (cursor_x, y), (cursor_x, y + self.font.get_height()))

    def main(self):
        running = True
        add_button = pygame.Rect(50, 120, 100, 50)
        start_button = pygame.Rect(50, 200, 100, 50)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if add_button.collidepoint(event.pos):
                        if self.input_text:
                            self.item_list.append(self.input_text)
                            self.input_text = ''
                    if start_button.collidepoint(event.pos):
                        print("List contents:")
                        for item in self.item_list:
                            print(item)
                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.backspace_timer = 0
                            if len(self.input_text) > 0:
                                self.input_text = self.input_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.input_text:
                                self.item_list.append(self.input_text)
                                self.input_text = ''
                        else:
                            if len(self.input_text) < 20:
                                self.input_text += event.unicode
                                self.cursor_timer = len(self.input_text)

                if event.type == pygame.KEYUP:
                    if self.input_active and event.key == pygame.K_BACKSPACE:
                        self.backspace_timer = 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        self.input_active = not self.input_active
                        self.cursor_timer = len(self.input_text)

            self.window.fill(self.WHITE)

            # Draw buttons
            pygame.draw.rect(self.window, self.BUTTON_COLOR_ADD, add_button)
            pygame.draw.rect(self.window, self.BUTTON_COLOR_START, start_button)

            # Draw text and cursor
            self.draw_text("Add", 75, 135)
            self.draw_text("Start", 70, 215)

            # Draw input box
            pygame.draw.rect(self.window, self.input_color, self.input_rect, 2)

            if self.input_active:
                self.draw_text(self.input_text, self.input_rect.x + 5, self.input_rect.y + 5)
                self.draw_cursor(self.input_rect.x + 5, self.input_rect.y + 5, self.input_text)

                # Hold backspace to remove multiple characters
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE]:
                    if self.backspace_timer == 0:
                        # Initial delay before starting character removal
                        if time.time() - self.backspace_start_time >= 1:  # 1 second delay
                            self.backspace_timer = self.initial_backspace_delay
                    elif self.backspace_timer > 0:
                        self.backspace_timer -= 1
                        if self.backspace_timer % self.backspace_interval == 0:
                            if len(self.input_text) > 0:
                                self.input_text = self.input_text[:-1]
                else:
                    self.backspace_timer = 0  # Reset the backspace timer if the key is released

            pygame.display.flip()

            # Limit the frame rate
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    list_manager = ListManager()
    while True:
        list_manager.backspace_start_time = time.time()
        list_manager.main()
        break
