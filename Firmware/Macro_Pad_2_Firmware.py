"""

  Macro_Keypad_2.0 Firmware

  Created by Michael Stickels
  
  Last Updated: *Unreleased*

  GPL-3.0 License



Seeeduino XIAO pin assignments:
    D0  - Keypad row 3
    D1  - Keypad row 2
    D2  - Keypad row 1
    D3  - DRGB LED
    D4  - Keypad column 1
    D5  - Keypad column 2
    D6  - Keypad column 3
    A7  - Slider pot 3
    A8  - Slider pot 2
    A9  - Slider pot 1
    D10 - Button

   
Button Layout:
    
    +-----------------+ +-----------------+ +-----------------+
    |                 | |                 | |                 |
    |        1        | |        3        | |        2        |
    |                 | |                 | |  Sound Switch   |
    |       F15       | |       F16       | |       F14       |
    |                 | |                 | |                 |
    +-----------------+ +-----------------+ +-----------------+
    +-----------------+ +-----------------+ +-----------------+
    |                 | |                 | |                 |
    |        4        | |        5        | |        6        |
    |   Xbox Overlay  | |     Record      | |   30s Replay    |
    |      WIN+G      | |    WIN+ALT+R    | |   WIN+ALT+G     |
    |                 | |                 | |                 |
    +-----------------+ +-----------------+ +-----------------+
    +-----------------+ +-----------------+ +-----------------+
    |                 | |                 | |                 |
    |        7        | |        8        | |        9        |
    |      Mute       | |   Screenshot    | |  Print Screen   |
    |       F13       | | WIN+ALT+PRTSCRN | |CRTL+ALT+PRTSCRN |
    |                 | |                 | |                 |
    +-----------------+ +-----------------+ +-----------------+

  

"""

import adafruit_matrixkeypad
import board
import time
import usb_hid
from analogio import AnalogIn
from digitalio import DigitalInOut
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


# Setup and initialize 3x3 matrix keypad
cols = [DigitalInOut(x) for x in (board.D0, board.D1, board.D2)]
rows = [DigitalInOut(x) for x in (board.D6, board.D5, board.D4)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
last_pressed = []


# Initialize HID keyboard input
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
kbd = Keyboard(usb_hid.devices)


# Initialize Deej sliders
slider_pins = [AnalogIn(board.A9), AnalogIn(board.A8), AnalogIn(board.A7)]
coefficient = 1023 / 1023**2


# Keyboard input helper
def send_keys(x):
    if x == 1:    kbd.send(Keycode.F15)
    elif x == 2:  kbd.send(Keycode.F16)
    elif x == 3:  kbd.send(Keycode.F14)
    elif x == 4:  kbd.send(Keycode.GUI, Keycode.G)
    elif x == 5:  kbd.send(Keycode.GUI, Keycode.ALT, Keycode.R)
    elif x == 6:  kbd.send(Keycode.GUI, Keycode.ALT, Keycode.G)
    elif x == 7:  kbd.send(Keycode.F13)
    elif x == 8:  kbd.send(Keycode.GUI, Keycode.ALT, Keycode.PRINT_SCREEN)
    elif x == 9:  kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN)


# Deej Helper
def get_voltage(pin):
    return round(coefficient * pow(pin.value * 1023 / 65535 - 1023, 2))



while True:
    
    # Keypad handler
    keys = keypad.pressed_keys
    if keys:
        temp = []
        for element in keys:
            if element not in last_pressed:
                temp.append(element)
        if len(temp) > 0:
            send_keys(temp[0])
    last_pressed = keys

    # Deej handler
    print_string = ""
    for pin in slider_pins:
        print_string += str(get_voltage(pin))
        if pin != slider_pins[-1]: print_string += "|"
    print(print_string)



    time.sleep(0.1)
