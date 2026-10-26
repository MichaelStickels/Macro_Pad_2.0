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


class Media:
    """Marks a key as a media key (sent via ConsumerControl, not Keyboard).

    Keycodes and ConsumerControlCodes are both plain ints, so code.py can't
    tell them apart on its own. Wrapping media keys in Media(...) labels them.
    """
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return "Media({})".format(self.code)


# Macros
# One entry per key, in order (key 1 first). Each entry is a list of keys that
# are pressed all at once (a chord), then released.
# - Normal keys:  Keycode.X        e.g. [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]
# - Media keys:   Media(ConsumerControlCode.X)   e.g. [Media(ConsumerControlCode.PLAY_PAUSE)]
# Key reference: https://docs.circuitpython.org/projects/hid/en/latest/api.html
# Keycode.GUI is the Windows key
MACROS = [
    [Keycode.ALT, Keycode.Z],                           # 1: Open Radeon sidebar
    [Media(ConsumerControlCode.PLAY_PAUSE)],            # 2: Play / pause
    [Keycode.GUI, Keycode.CONTROL, Keycode.V],          # 3: Open speaker select
    [Keycode.CONTROL, Keycode.SHIFT, Keycode.E],        # 4: Toggle recording
    [Keycode.CONTROL, Keycode.SHIFT, Keycode.S],        # 5: Save instant replay
    [Keycode.CONTROL, Keycode.SHIFT, Keycode.J],        # 6: Save GIF replay
    [Keycode.F16],                                      # 7: Mute (or: Media(ConsumerControlCode.MUTE))
    [Keycode.CONTROL, Keycode.ALT, Keycode.I],          # 8: Save screenshot to disk
    [Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN],  # 9: Screenshot to clipboard
]

# Spare macros, swap into the list above if you want them
# [Keycode.CONTROL, Keycode.ALT, Keycode.K]
# [Keycode.CONTROL, Keycode.SHIFT, Keycode.O]           # Toggle FPS overlay

# RGB
RGB_mode = 'rainbow'  # 'rainbow' or 'solid'
RGB_color = (255, 0, 0)  # RGB value for solid color
RGB_brightness = 0.12  # Between 0.0 and 1.0
