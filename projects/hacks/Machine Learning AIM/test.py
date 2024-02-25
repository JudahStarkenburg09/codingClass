import win32gui, win32ui
from win32api import GetSystemMetrics

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

while True:
    #               x1,y1,x2,y2
    dcObj.DrawFocusRect((0,0,100,100))
    win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor