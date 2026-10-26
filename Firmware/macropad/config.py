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
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Macros
# Set your macros here. All keys simultaneously (rather than one at a time)
# Separate each key with a comma
# Key reference can be found at https://docs.circuitpython.org/projects/hid/en/latest/api.html
# Keycode.GUI is the Windows key
# MACRO_1 = [Keycode.CONTROL, Keycode.ALT, Keycode.K]
MACRO_1 = [Keycode.ALT, Keycode.Z]                                  # Open Radeon sidebar
# MACRO_2 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.O]               # Toggle FPS overlay
MACRO_2 = [ConsumerControlCode.PLAY_PAUSE]
MACRO_3 = [Keycode.GUI, Keycode.CONTROL, Keycode.V]                 # Open speaker select
MACRO_4 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]               # Toggle recording
MACRO_5 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.S]               # Save instant replay
MACRO_6 = [Keycode.CONTROL, Keycode.SHIFT, Keycode.J]               # Save GIF replay
MACRO_7 = [Keycode.F16]                                             # Mute
MACRO_8 = [Keycode.CONTROL, Keycode.ALT, Keycode.I]                 # Save screenshot to disk
MACRO_9 = [Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN]      # Screenshot to clipboard

# RGB
RGB_mode = 'rainbow'  # 'rainbow' or 'solid'
RGB_color = (255,0,0) # RGB value for solid color
RGB_brightness = 0.12  # Between 0.0 and 1.0