import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")
            
import time



lp = launchpad.Launchpad()
if lp.Open():
    print("Launchpad Mk1/S/Mini")
    mode = "Mk1"

lp.ButtonFlush()
lp.Reset()

def resetBoard():
    global LaunchpadBoard
    LaunchpadBoard = [
    {0: [0, 0]}, {1: [0, 0]}, {2: [0, 0]}, {3: [0, 0]}, {4: [0, 0]}, {5: [0, 0]}, {6: [0, 0]}, {7: [0, 0]},
    {16: [0, 0]}, {17: [0, 0]}, {18: [0, 0]}, {19: [0, 0]}, {20: [0, 0]}, {21: [0, 0]}, {22: [0, 0]}, {23: [0, 0]},
    {32: [0, 0]}, {33: [0, 0]}, {34: [0, 0]}, {35: [0, 0]}, {36: [0, 0]}, {37: [0, 0]}, {38: [0, 0]}, {39: [0, 0]},
    {48: [0, 0]}, {49: [0, 0]}, {50: [0, 0]}, {51: [0, 0]}, {52: [0, 0]}, {53: [0, 0]}, {54: [0, 0]}, {55: [0, 0]},
    {64: [0, 0]}, {65: [0, 0]}, {66: [0, 0]}, {67: [0, 0]}, {68: [0, 0]}, {69: [0, 0]}, {70: [0, 0]}, {71: [0, 0]},
    {80: [0, 0]}, {81: [0, 0]}, {82: [0, 0]}, {83: [0, 0]}, {84: [0, 0]}, {85: [0, 0]}, {86: [0, 0]}, {87: [0, 0]},
    {96: [0, 0]}, {97: [0, 0]}, {98: [0, 0]}, {99: [0, 0]}, {100: [0, 0]}, {101: [0, 0]}, {102: [0, 0]}, {103: [0, 0]},
    {112: [0, 0]}, {113: [0, 0]}, {114: [0, 0]}, {115: [0, 0]}, {116: [0, 0]}, {117: [0, 0]}, {118: [0, 0]}, {119: [0, 0]}
    ]



def set_button_color(button_number, color):
    global LaunchpadBoard
    for item in LaunchpadBoard:
        if button_number in item:
            item[button_number] = color
            lp.LedCtrlRaw(button_number, item)



while True:
    resetBoard()
    lp.Reset()

    # Example usage:
    # Set button number 1 to yellow ([3, 3])
    set_button_color(1, [3, 3])

    # Set button number 16 to red ([3, 0])
    set_button_color(16, [3, 0])

    # Set button number 32 to green ([0, 3])
    set_button_color(32, [0, 3])

    time.sleep(0.01) # Pause to reduce CPU usage

