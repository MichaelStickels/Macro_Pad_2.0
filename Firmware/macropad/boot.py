"""

    Macro_Keypad_2.0 Firmware

    Created by Michael Stickels

    Last Updated: *Unreleased*

    GPL-3.0 License

"""

import storage
import board, digitalio

# Rename drive for ease of use
new_name = "macropad"
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = new_name
storage.remount("/", readonly=True)

# Enable USB storage only if button is pressed at boot
button = digitalio.DigitalInOut(board.D7)
button.pull = digitalio.Pull.UP
if button.value:
    storage.disable_usb_drive()

