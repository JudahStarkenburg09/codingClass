import pygame



def rightJSAxis():
    right_x_axis = 0
    right_y_axis = 0

    pygame.event.get()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    for joystick in joysticks:
        left_x_axis = joystick.get_axis(0)
        left_y_axis = joystick.get_axis(1)
        right_x_axis = joystick.get_axis(2)
        right_y_axis = joystick.get_axis(3)


    

    return right_x_axis, right_y_axis


def leftJSAxis():
    left_x_axis = 0
    left_y_axis = 0

    pygame.event.get()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


    for joystick in joysticks:
        left_x_axis = joystick.get_axis(0)
        left_y_axis = joystick.get_axis(1)
        right_x_axis = joystick.get_axis(2)
        right_y_axis = joystick.get_axis(3)


    return left_x_axis, left_y_axis

def getPressedButtons():
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

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                button_pressed = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_pressed:
                        return correspond["button"], correspond["correspond"]
            elif event.type == pygame.JOYBUTTONUP:
                button_released = event.button
                for correspond in buttonsCorrespondings:
                    if correspond["button"] == button_released:
                        return correspond["button"], correspond["correspond"]


def convertJSAxisToCoords(centerX, centerY, radius, axisX, axisY):
    # Calculate the position based on joystick input
    max_displacement = radius  # Maximum displacement for the joystick
    new_x = centerX + int(max_displacement * axisX)
    new_y = centerY + int(max_displacement * axisY)

    # Ensure the joystick stays within the specified bounds
    if new_x < (centerX - radius):
        new_x = centerX - radius
    elif new_x > (centerX + radius):
        new_x = centerX + radius
    if new_y < (centerY - radius):
        new_y = centerY - radius
    elif new_y > (centerY + radius):
        new_y = centerY + radius

    return new_x, new_y

pygame.init()
pygame.joystick.init()

while True:
    leftJoystickPos = leftJSAxis()
    print(leftJoystickPos)

