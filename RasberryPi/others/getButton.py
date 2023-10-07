import pygame
pygame.init()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            axis_id = event.axis
            axis_value = event.value
            
            if axis_id == 2:
                # R2 axis
                print(f"R2 Axis: {axis_value}")
            elif axis_id == 5:
                # L2 axis
                print(f"L2 Axis: {axis_value}")
