import pygame

pygame.init()

# Initialize the joystick
j = pygame.joystick.Joystick(0)
j.init()

# Define the button correspondences
buttonsCorrespondings = [
    {
        "button": 0,
        "correspond": "X",
    },
    {
        "button": 1,
        "correspond": "O",
    },
    {
        "button": 2,
        "correspond": "Square",
    },
    {
        "button": 3,
        "correspond": "Triangle",
    },
    {
        "button": 4,
        "correspond": "Share",
    },
    {
        "button": 6,
        "correspond": "Options",
    },
    {
        "button": 7,
        "correspond": "Left Joystick PRESS",
    },
    {
        "button": 8,
        "correspond": "Right Joystick PRESS",
    },
    {
        "button": 9,
        "correspond": "L1",
    },
    {
        "button": 10,
        "correspond": "R1",
    },
    {
        "button": 11,
        "correspond": "Directional Button Up",
    },
    {
        "button": 12,
        "correspond": "Directional Button Down",
    },
    {
        "button": 13,
        "correspond": "Directional Button Left",
    },
    {
        "button": 14,
        "correspond": "Directional Button Right",
    },
    {
        "button": 15,
        "correspond": "Touchpad Click",
    },
]

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                button_pressed = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_pressed:
                        print(f"Button {correspond['correspond']} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                button_released = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_released:
                        print(f"Button {correspond['correspond']} released")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
