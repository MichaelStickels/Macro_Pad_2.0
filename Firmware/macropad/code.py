"""

    Macro_Keypad_2.0 Firmware

    Created by Michael Stickels

    Last Updated: *Unreleased*

    GPL-3.0 License


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


# Pin assignments (preset for Xiao RP2040)
KEY_COL_1 = board.D10
KEY_COL_2 = board.D9
KEY_COL_3 = board.D8
KEY_ROW_1 = board.D5
KEY_ROW_2 = board.D4
KEY_ROW_3 = board.D3
SLIDER_1 = board.A0
SLIDER_2 = board.A1
SLIDER_3 = board.A2
RGB_DATA = board.D6
BUTTON = board.D7

# Initializations ------------------------------------------------------------

# Setup and initialize 3x3 matrix keypad
cols = [DigitalInOut(x) for x in (KEY_COL_1, KEY_COL_2, KEY_COL_3)]
rows = [DigitalInOut(x) for x in (KEY_ROW_1, KEY_ROW_2, KEY_ROW_3)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
last_pressed = []

# Initialize HID keyboard input
time.sleep(1)  # Sleep for a moment to avoid a race condition on some systems (according to Adafruit)
kbd = Keyboard(usb_hid.devices)

# Initialize Deej sliders
slider_pins = [AnalogIn(SLIDER_1), AnalogIn(SLIDER_2), AnalogIn(SLIDER_3)]

# Initialize RGB
pixel_pin = RGB_DATA
num_pixels = 51
RGB_brightness = config.RGB_brightness
RGB_mode = config.RGB_mode
RGB_color = config.RGB_color
off = (0,0,0)
RGB_tick = 0
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = RGB_brightness, auto_write = False)


# Helper Functions  ----------------------------------------------------------

# Keyboard input helper
def send_keys(x):
    if x == 1:
        for key in config.MACRO_1:
            kbd.press(key)
        kbd.release_all()
    elif x == 2:
        for key in config.MACRO_2:
            kbd.press(key)
        kbd.release_all()
    elif x == 3:
        for key in config.MACRO_3:
            kbd.press(key)
        kbd.release_all()
    elif x == 4:
        for key in config.MACRO_4:
            kbd.press(key)
        kbd.release_all()   
    elif x == 5:
        for key in config.MACRO_5:
            kbd.press(key)
        kbd.release_all()
    elif x == 6:
        for key in config.MACRO_6:
            kbd.press(key)
        kbd.release_all()
    elif x == 7:
        for key in config.MACRO_7:
            kbd.press(key)
        kbd.release_all()
    elif x == 8:
        for key in config.MACRO_8:
            kbd.press(key)
        kbd.release_all()
    elif x == 9:
        for key in config.MACRO_9:
            kbd.press(key)
        kbd.release_all()


# Deej Helper
# Adjusts response of linear potentiometers for finer low volume control
def get_voltage(pin):
    return round((1023 / 1023 ** 2) * pow(pin.value * 1023 / 65535 - 1023, 2))


# Rainbow RGB Helper
def rainbow_update(j):
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels) + j
        pixels[i] = colorwheel(rc_index & 255)
    pixels.show()


# Running loop ------------------------------------------------------------
while True:

    # Do functions only if USB connection is active
    if supervisor.runtime.usb_connected:    # checks USB connection

        # Keypad handler
        keys = keypad.pressed_keys
        if keys:                                # If any keys are pressed
            temp = []
            for element in keys:
                if element not in last_pressed:
                    temp.append(element)        # and any of those keys are newly pressed
            if len(temp) > 0:
                send_keys(temp[0])              # send input to computer.
        last_pressed = keys                     # Stops keys from repeating while held down.

        # Deej handler
        print_string = ""
        for pin in slider_pins:                     # read value of each slider
            print_string += str(get_voltage(pin))
            if pin != slider_pins[-1]:              # put into Deej format
                print_string += "|"
        print(print_string)                         # send to computer over serial

        # RGB update
        if RGB_mode == 'rainbow':
            if RGB_tick >= 256: RGB_tick = 0
            rainbow_update(RGB_tick)
            RGB_tick += 2
        else:
            pixels.fill(RGB_color)
            pixels.show()

    # If USB is not connected, turn off LEDs and don't bother sending data
    else:
        pixels.fill(off)
        pixels.show()
        time.sleep(5)


    # Slow the program down a smidge. There are better ways to do this, but this works for now
    time.sleep(0.1)
