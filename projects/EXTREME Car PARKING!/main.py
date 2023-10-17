import pygame
import os

currentCWD = os.getcwd()
os.chdir(os.path.join(currentCWD, 'data'))

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.trafficBarrier = pygame.image.load('trafficBarrier.png')
         
    def makeBarrier(self, x, y, angle):
        rotated_barrier = pygame.transform.rotate(self.trafficBarrier, angle)
        rect = rotated_barrier.get_rect(center=(x, y))
        self.screen.blit(rotated_barrier, rect.topleft)

    def levelOne(self):
        # Add your logic here
        pass

    def mainloop(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.screen.fill((255, 255, 255))  # Fill the screen with white

            # Game Login Here
            


            pygame.display.flip()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.mainloop()
