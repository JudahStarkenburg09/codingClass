import cv2
import numpy as np
import pyautogui
import time
import torch
import keyboard
import win32gui
import win32ui
import win32con
from win32api import GetSystemMetrics, RGB
import pydirectinput

model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'best.pt')
pydirectinput.PAUSE = 0.01


# Function to draw a red rectangle overlay on the screen
def draw_overlay_rectangle(x1, y1, x2, y2, thickness=1):
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0, 0))
    monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
    # Set the color to red
    dcObj.SetTextColor(RGB(0, 255, 0))  # Red color (RGB format: Red=255, Green=0, Blue=0)
    # Set the pen properties (thickness)
    pen = win32ui.CreatePen(win32con.PS_SOLID, thickness, RGB(0, 255, 0))  # Solid pen with specified thickness
    dcObj.SelectObject(pen)
    # Draw the rectangle overlay
    dcObj.DrawFocusRect((x1, y1, x2, y2))
    # Refresh the entire monitor to show the changes
    win32gui.InvalidateRect(hwnd, monitor, True)



isactive = False

def toggle_isactive():
    global isactive
    if not isactive:
        print("Turned on")
    else:
        print("Turned off")
    isactive = not isactive


# Register a callback for when the 'h' key is released
keyboard.on_release_key('h', lambda event: toggle_isactive())  # Corrected lambda function call

while True:
    if isactive:
        if keyboard.is_pressed(']'):
            if max_bbox is not None:
                x1, y1, x2, y2 = max_bbox[:4]
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)
                pydirectinput.moveTo(center_x, center_y, duration=0.1)

        # Capture screenshot and run model
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        model.conf = 0.10
        results = model(frame, size=640)

        # Find bounding box of largest confidence person
        class_names = results.names
        bboxes = results.xyxy[0].cpu().numpy()
        max_confidence = 0
        max_bbox = None
        for bbox in bboxes:
            if bbox[4] > max_confidence and class_names[int(bbox[5])] == 'Player':
                max_confidence = bbox[4]
                max_bbox = bbox

        # Draw bounding box overlay on the screen
        if max_bbox is not None:
            x1, y1, x2, y2 = max_bbox[:4]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers
            draw_overlay_rectangle(x1, y1, x2, y2)

    # Wait a bit to prevent high CPU usage
    time.sleep(0.001)
