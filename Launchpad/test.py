import launchpad_py as launchpad
import time


lp = launchpad.Launchpad()
if lp.Open():
    print("Launchpad Mk1/S/Mini")
    mode = "Mk1"


# lp.LedCtrlXY(0, 0, 1, 0)
# lp.LedCtrlAutomap(1, 2, 0)
lp.LedCtrlRaw(1, 0, 5)

time.sleep(2)

lp.Reset() # turn all LEDs off
lp.Close()