"""

  Macro_Keypad_2.0 Configuration

  Created by Michael Stickels

  Last Updated: *Unreleased*

  GPL-3.0 License


Keyswitch Layout:

    +-------------+ +-------------+ +-------------+
    |             | |             | |             |
    |      1      | |      2      | |      3      |
    |             | |             | |             |
    +-------------+ +-------------+ +-------------+
    +-------------+ +-------------+ +-------------+
    |             | |             | |             |
    |      4      | |      5      | |      6      |
    |             | |             | |             |
    +-------------+ +-------------+ +-------------+
    +-------------+ +-------------+ +-------------+
    |             | |             | |             |
    |      7      | |      8      | |      9      |
    |             | |             | |             |
    +-------------+ +-------------+ +-------------+

"""
from adafruit_hid.keycode import Keycode

# Macros
# Set your macros here. All keys simultaneously (rather than one at a time)
# Separate each key with a comma
# Key reference can be found at https://docs.circuitpython.org/projects/hid/en/latest/api.html
# Keycode.GUI is the Windows key
MACRO_1 = [Keycode.ALT, Keycode.Z]
MACRO_2 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.O] 
MACRO_3 = [Keycode.GUI, Keycode.CONTROL, Keycode.V]
MACRO_4 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.E] 
MACRO_5 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.S]
MACRO_6 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.J]
MACRO_7 = [Keycode.F16]
MACRO_8 = [Keycode.GUI, Keycode.ALT, Keycode.PRINT_SCREEN]
MACRO_9 = [Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN]

# RGB
RGB_mode = 'rainbow'  # 'rainbow' or 'solid'
RGB_color = (255,0,0) # RGB value for solid color
RGB_brightness = 0.12  # Between 0.0 and 1.0