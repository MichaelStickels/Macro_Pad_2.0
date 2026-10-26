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
from adafruit_hid.consumer_control import ConsumerControl
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

# Timing (seconds). Keys are scanned fast so short taps aren't missed;
# sliders and LEDs update on their own slower schedules.
KEY_SCAN_INTERVAL = 0.01
DEEJ_INTERVAL = 0.1
RGB_INTERVAL = 0.05

NUM_KEYS = 9
NUM_PIXELS = 51
OFF = (0, 0, 0)

# Catch config mistakes at boot instead of on the first keypress
if len(config.MACROS) != NUM_KEYS:
    raise ValueError("config.MACROS must have {} entries, found {}".format(
        NUM_KEYS, len(config.MACROS)))

# Initializations ------------------------------------------------------------

# Setup and initialize 3x3 matrix keypad
cols = [DigitalInOut(x) for x in (KEY_COL_1, KEY_COL_2, KEY_COL_3)]
rows = [DigitalInOut(x) for x in (KEY_ROW_1, KEY_ROW_2, KEY_ROW_3)]
key_layout = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, key_layout)
last_pressed = []

# Initialize HID devices
time.sleep(1)  # Avoids a race condition on some systems (according to Adafruit)
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# Initialize Deej sliders
slider_pins = [AnalogIn(SLIDER_1), AnalogIn(SLIDER_2), AnalogIn(SLIDER_3)]

# Initialize RGB
pixels = neopixel.NeoPixel(RGB_DATA, NUM_PIXELS,
                           brightness=config.RGB_brightness, auto_write=False)
rgb_tick = 0


# Helper Functions  ----------------------------------------------------------

def send_macro(macro):
    """Press every key in the macro at once, then release them all.

    Plain ints are keyboard keys; config.Media(...) entries are media keys.
    """
    kb_keys = [k for k in macro if not isinstance(k, config.Media)]
    media_codes = [k.code for k in macro if isinstance(k, config.Media)]
    try:
        if kb_keys:
            kbd.press(*kb_keys)
        for code in media_codes:
            cc.press(code)
    finally:
        # Always release, even if something above failed, so no key gets stuck
        kbd.release_all()
        if media_codes:
            cc.release()


def send_keys(x):
    """Send the macro for key number x (1-9)."""
    send_macro(config.MACROS[x - 1])


# Deej Helper
# Adjusts response of linear potentiometers for finer low volume control
def get_voltage(pin):
    return round((1023 / 1023 ** 2) * pow(pin.value * 1023 / 65535 - 1023, 2))


# Rainbow RGB Helper
def rainbow_update(j):
    for i in range(NUM_PIXELS):
        rc_index = (i * 256 // NUM_PIXELS) + j
        pixels[i] = colorwheel(rc_index & 255)
    pixels.show()


def update_keys():
    global last_pressed
    pressed = keypad.pressed_keys
    for key in pressed:
        if key not in last_pressed:     # newly pressed (not held from before)
            send_keys(key)
    last_pressed = pressed


def update_deej():
    line = "|".join(str(get_voltage(pin)) for pin in slider_pins)
    print(line)  # Deej reads this over serial


def update_rgb():
    global rgb_tick
    if config.RGB_mode == 'rainbow':
        rainbow_update(rgb_tick)
        rgb_tick = (rgb_tick + 2) % 256
    else:
        pixels.fill(config.RGB_color)
        pixels.show()


# Running loop ------------------------------------------------------------
next_deej = 0
next_rgb = 0

while True:

    # Do functions only if USB connection is active
    if supervisor.runtime.usb_connected:
        now = time.monotonic()

        update_keys()

        if now >= next_deej:
            update_deej()
            next_deej = now + DEEJ_INTERVAL

        if now >= next_rgb:
            update_rgb()
            next_rgb = now + RGB_INTERVAL

        time.sleep(KEY_SCAN_INTERVAL)

    # If USB is not connected, turn off LEDs and don't bother sending data
    else:
        pixels.fill(OFF)
        pixels.show()
        time.sleep(5)