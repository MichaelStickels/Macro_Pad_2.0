"""

  Macro_Keypad_2.0 Firmware

  Created by Michael Stickels

  Last Updated: *Unreleased*

  GPL-3.0 License



Seeeduino RP2040 pin assignments:
    D3  - Keypad row 1
    D4  - Keypad row 2
    D5  - Keypad row 3
    D6  - DRGB LED
    D10 - Keypad column 1
    D9  - Keypad column 2
    D8  - Keypad column 3
    A0  - Slider pot 3
    A1  - Slider pot 2
    A2  - Slider pot 1
    D7 - Button


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

import config
import adafruit_matrixkeypad
import supervisor
import board
import time
import usb_hid
import neopixel
from analogio import AnalogIn
from digitalio import DigitalInOut
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from rainbowio import colorwheel



# Setup and initialize 3x3 matrix keypad
cols = [DigitalInOut(x) for x in (board.D10, board.D9, board.D8)]
rows = [DigitalInOut(x) for x in (board.D5, board.D4, board.D3)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
last_pressed = []


# Initialize HID keyboard input
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
kbd = Keyboard(usb_hid.devices)


# Initialize Deej sliders
slider_pins = [AnalogIn(board.A0), AnalogIn(board.A1), AnalogIn(board.A2)]


# Initialize RGB
pixel_pin = board.D6
num_pixels = 51
RGB_brightness = 0.2
RGB_tick = 0
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = RGB_brightness, auto_write = False)



# Keyboard input helper
def send_keys(x):
    if x == 1:
        kbd.send(Keycode.F15)
    elif x == 2:
        kbd.send(Keycode.F16)
    elif x == 3:
        kbd.send(Keycode.F14)
    elif x == 4:
        kbd.send(Keycode.GUI, Keycode.G)
    elif x == 5:
        kbd.send(Keycode.GUI, Keycode.ALT, Keycode.R)
    elif x == 6:
        kbd.send(Keycode.GUI, Keycode.ALT, Keycode.G)
    elif x == 7:
        kbd.send(Keycode.F13)
    elif x == 8:
        kbd.send(Keycode.GUI, Keycode.ALT, Keycode.PRINT_SCREEN)
    elif x == 9:
        kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN)


# Deej Helper
def get_voltage(pin):
    return round((1023 / 1023 ** 2) * pow(pin.value * 1023 / 65535 - 1023, 2))


# RGB Helpers
def rainbow_cycle(j):
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels) + j
        pixels[i] = colorwheel(rc_index & 255)
    pixels.show()


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
        if pin != slider_pins[-1]:
            print_string += "|"
    print(print_string)

    # Update RGB only if USB is connected
    if supervisor.runtime.usb_connected:    # USB Connected
        if RGB_tick == 256: RGB_tick = 0
        rainbow_cycle(RGB_tick)
        RGB_tick += 1  
    else:                                   # no USB
        pixels.fill((0, 0, 0))
        pixels.show   
        
    # Slow the program down a smidge. Is this necessary? Maybe?
    time.sleep(0.1)
