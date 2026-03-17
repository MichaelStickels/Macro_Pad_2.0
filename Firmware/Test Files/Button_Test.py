# Example code from Adafruit debounce library

# SPDX-FileCopyrightText: 2019 Dave Astels for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
from adafruit_debouncer import Debouncer

pin = digitalio.DigitalInOut(board.D10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.DOWN
switch = Debouncer(pin)

while True:
    switch.update()
    if switch.fell:
        print("Just released")
    if switch.rose:
        print("Just pressed")