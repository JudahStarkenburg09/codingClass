#!/usr/bin/env python

import sys
from pygame import time

try:
    import launchpad_py as launchpad
except ImportError:
    sys.exit("Error loading launchpad.py")

def main():
    # create an instance for Launchpad Mk1
    lp = launchpad.Launchpad()

    if lp.Open():
        print("Launchpad Mk1")

        # Clear the buffer
        lp.ButtonFlush()

        print("Waiting for button inputs. Press Ctrl+C to exit.")

        while True:
            # Check for button events
            buttons = lp.ButtonStateRaw()

            if buttons:
                print("Button event:", buttons)

            # Wait for a short duration to avoid high CPU usage
            time.wait(5)

    else:
        print("Did not find any Launchpad Mk1.")

    # Cleanup
    lp.Close()

if __name__ == '__main__':
    main()
